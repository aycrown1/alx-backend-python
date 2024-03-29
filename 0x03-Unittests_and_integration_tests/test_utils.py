#!/usr/bin/env python3
"""
This module is a unittesting module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Create a TestAccessNestedMap class that inherits
        from unittest.TestCase
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """
        method to test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """
        Use the assertRaises context manager to test that a KeyError
        is raised for the following inputs
            (use @parameterized.expand):
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """implement the TestGetJson.test_get_json method"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """
        method to test that utils.get_json returns the expected result.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """the TestMemoize(unittest.TestCase) class
    with a test_memoize method."""

    def test_memoize(self) -> None:
        """define class TestClass"""

        class TestClass:
            """unittest.mock.patch class"""

            def a_method(self) -> int:
                """unittest.mock.patch method"""
                return 42

            @memoize
            def a_property(self) -> int:
                """unittest.mock.patch method"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
