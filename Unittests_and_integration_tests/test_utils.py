#!/usr/bin/env python3
""" Task 0
"""

import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ Tests access_nested_map function """

    @parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Testing result """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Testing error """
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests get_json function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, testUrl, test_payload):
        """ Testing get_json """
        with mock.patch('requests.get', return_value=mock.Mock(
                json=lambda: test_payload)):
            self.assertEqual(get_json(testUrl), test_payload)
