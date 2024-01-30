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
        """ Testing public repo results """
        test_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          filler=PropertyMock) as mk:
            mk.return_value = "www.test.com"
            test = GithubOrgClient("test")
            result = test.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mk.assert_called_once()
            test_json.assert_called_once()
