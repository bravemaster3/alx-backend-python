#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
Default = Union[T, None]
Retrn = Union[Any, T]


def safely_get_value(
        dct: Mapping, key: Any, default: Default = None
) -> Retrn:
    """ gets value from dictionary safely """
    if key in dct:
        return dct[key]
    else:
        return default
