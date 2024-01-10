#!/usr/bin/env python3
"""Function that gets a range of indexes
   for particular pagination parameters
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """Returns a range of indexes"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)