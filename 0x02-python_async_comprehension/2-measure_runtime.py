#!/usr/bin/env python3
""" Measures the runtine of Async comprehension """
from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a measure_runtime coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather

    """
    tasks = []
    measure_time_start = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    measure_time_end = time.time()
    return measure_time_end - measure_time_start
