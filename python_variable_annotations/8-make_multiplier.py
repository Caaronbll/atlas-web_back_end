#!/usr/bin/env python3

"""function that multiplies"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters: float value
    Returns: Function that multiplies
    """
    def return_multiplier(x: float) -> float:
        return x * multiplier

    return return_multiplier