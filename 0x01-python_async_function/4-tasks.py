#!/usr/bin/env python3
"""
This module write an asynchronous coroutine for the function
task_wait_n
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The function that takes in 2 int arguments (in this order):
         n and max_delay.
         You will spawn task_wait_random n times with the specified max_delay.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
