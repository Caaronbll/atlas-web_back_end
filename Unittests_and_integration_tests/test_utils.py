#!/usr/bin/env python3
""" Task 0
"""

import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """ Tests access class """

    @parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Testing access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)
