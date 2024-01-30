#!/usr/bin/env python3
""" Task 4
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch, PropertyMock
import requests
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ Tests GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, test_json):
        """ Testing return value """
        client = GithubOrgClient(org)
        client_return = client.org
        self.assertEqual(client_return, test_json.return_value)

    def test_public_repos_url(self):
        """ Testing public URLs """
        with patch('client.GithubOrgClient.org',
            filler=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://testurl.com"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "http://testurl.com")

    @patch('client.get_json')
    def test_public_repos(self, test_json):
        """ Testing public repo responses """
        values = [{"name": "Hey"}, {"name": "Dude"}]
        test_json.return_value = values

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Hey", "Dude"])

            mocked_public.assert_called_once()
            test_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """ Testing license results """
        self.assertEqual(GithubOrgClient.has_license(repo, key),
                         expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Tests set-up and tear down
    of GithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """ Set up the class """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mocking the behavior of requests.get for different URLs
        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload),
            unittest.mock.Mock(json=lambda: cls.expected_repos),
            unittest.mock.Mock(json=lambda: cls.apache2_repos),
        ]

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

    @parameterized_class
    def test_public_repos(self):
        """ Testing public_repos """
        client = GithubOrgClient("test")
        repos = client.public_repos()

        # Assertions based on the expected data
        self.assertEqual(repos, self.expected_repos)
