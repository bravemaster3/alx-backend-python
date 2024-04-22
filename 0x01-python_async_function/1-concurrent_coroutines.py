#!/usr/bin/env python3
"""
wait_n that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async function that returns a list of n random floats """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, pending = await asyncio.wait(tasks)
    return [task.result() for task in completed]
