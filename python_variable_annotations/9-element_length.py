#!/usr/bin/env python3

"""annotating the given function"""

from typing import Tuple

def element_length(lst: int) -> Tuple:
    """
    Parameters: 1st
    Returns: tuple?
    """
    return [(i, len(i)) for i in lst]