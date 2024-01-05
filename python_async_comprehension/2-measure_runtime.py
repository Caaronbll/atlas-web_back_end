#!/usr/bin/env python3

"""task 2"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Parameters: none
    Returns: time
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    runtime = end_time - start_time
    return runtime