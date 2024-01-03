#!/usr/bin/env python3

"""sums up a list of floats"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Parameters: input list
    Returns: sum as a float
    """
    return sum(mxd_lst)