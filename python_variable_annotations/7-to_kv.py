#!/usr/bin/env python3

"""creates a tuple of a string and an int or float"""


from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert key-value pair to tuple where v is squared
    :param k: key
    :param v: value
    :return: tuple
    """
    return (k, (v) ** 2)