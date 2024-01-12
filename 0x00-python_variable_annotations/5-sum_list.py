#!/usr/bin/env python3
"""
This module defined a type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list function which takes a list input_list
            of floats as argument and returns their sum as a float.
    """
    return sum(input_list)
