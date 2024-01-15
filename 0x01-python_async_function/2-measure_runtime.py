#!/usr/bin/env python3
"""
This module writes an asynchronous coroutine for a function:
    measure_time
"""
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines.').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n
