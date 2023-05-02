#!/usr/bin/env python3
""" The basics of async  """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
"""Delay betweent 0 and Max_dalar"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
