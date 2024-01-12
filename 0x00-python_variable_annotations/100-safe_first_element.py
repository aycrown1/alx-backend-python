#!/usr/bin/env python3
"""
This module defined a type-annotated function safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    safe_first_element function augmented with
    the correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
