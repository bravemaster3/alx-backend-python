#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """class for testing get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ], names=["test_url", "test_payload"])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test get_json method"""
        # Create a Mock object for the JSON response
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the return value of the mock get method to be the mock response
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that requests.get was called with the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """class definition"""
    def test_memoize(self):
        """method test_memoize definitino"""
        class TestClass:
            """class testclass definition"""
            def a_method(self):
                "method definition"
                return 42

            @memoize
            def a_property(self):
                """method definition"""
                return self.a_method()

        obj = TestClass()
        with patch.object(obj, 'a_method', return_value=42) as mock_a_method:
            result1 = obj.a_property
            result2 = obj.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
