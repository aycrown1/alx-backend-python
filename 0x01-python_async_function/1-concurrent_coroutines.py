#!/usr/bin/env python3
"""
This module writes an asynchronous coroutine function
wait_n
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    The function that takes in 2 int arguments (in this order):
         n and max_delay.
         You will spawn wait_random n times with the specified max_delay.
    """
    delays: float = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
