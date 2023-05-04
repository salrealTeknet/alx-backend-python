#!/usr/bin/env python3
""" Measures the runtine of Async comprehension """
from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ a measure_runtime coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather
    """
    s = time.perf_counter()
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    elapsed = time.perf_counter() - s
    return elapsed
