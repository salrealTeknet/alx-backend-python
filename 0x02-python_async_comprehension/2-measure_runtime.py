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
    start_time = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
