#!/usr/bin/env python3
"""
This module defined a type-annotated function element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    annotation of element_length function
    """
    return [(i, len(i)) for i in lst]
