#!/usr/bin/env python3
"""task 4"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters: n a number and delay
    Returns: list
    """
    delays: List[float] = []

    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    new_list: List[float] = []

    while delays:
        min = delays[0]
        for x in delays:
            if x < min:
                min = x
        new_list.append(min)
        delays.remove(min)

    return new_list