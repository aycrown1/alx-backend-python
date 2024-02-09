#!/usr/bin/env python3
"""
This module is a unittesting module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict


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
