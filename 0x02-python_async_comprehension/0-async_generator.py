#!/usr/bin/env python3
"""Contains a coroutine that takes no arguments, loops 10 times awaiting 1 sec each then yield a random no."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        Generates random numbers
        Args:
            void
        Return:
            float time random
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
