#!/usr/bin/env python3

"""task 1"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Parameters: none
    Returns: random numbers
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]