#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and
returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]]) -> float:
    """sums a list of floats"""
    return sum(mxd_lst)
