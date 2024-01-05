#!/usr/bin/env python3

"""task 0"""
import asyncio, random


async def async_generator():
    """
    Parameters: none
    Returns: 10 random numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)