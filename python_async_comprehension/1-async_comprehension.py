#!/usr/bin/env python3

"""task 1"""
import asyncio, random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Parameters: none
    Returns: random numbers
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]