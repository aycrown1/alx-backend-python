#!/usr/bin/env python3
"""
This module defined a type-annotated function safely_get_value
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    safely_get_value function, updated with type-annotation
    """
    if key in dct:
        return dct[key]
    else:
        return default
