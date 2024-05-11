#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class definition"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ], names=["nested_map", "path", "expected_result"])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """tests that the method gives expected outputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ], names=["nested_map", "path"])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests that the method raises error"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
