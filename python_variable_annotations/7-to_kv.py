#!/usr/bin/env python3

"""creates a tuple of a string and an int or float"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """
    Parameters: string and a float or int
    Returns: tuple
    """
    return (k, float(v) ** 2.0)