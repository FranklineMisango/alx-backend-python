#!/usr/bin/env python3
"""Has a coroutine that delays a certain amount of time and eventually returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float between 0 and max_delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    """

    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return
