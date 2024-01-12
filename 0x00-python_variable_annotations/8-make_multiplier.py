#!/usr/bin/env python3
"""
This module defined a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    """
    def multiplier_function(value: float) -> float:
        """
        multiplier_function multiplies a float by multiplier
        """
        return value * multiplier
    return multiplier_function
