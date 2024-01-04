#!/usr/bin/env python3

"""annotating the given function"""

from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Parameters: list
    Returns: list of tuples
    """
    return [(i, len(i)) for i in lst]