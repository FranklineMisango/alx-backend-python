#!/usr/bin/env python3
"""Measure the times"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measures time and executes in parallel
        Args:
            void
        Return:
            float random numbers
    """
    first_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter()

    return (elapsed - first_time)
