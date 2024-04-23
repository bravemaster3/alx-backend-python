#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
 then yield a random number between 0 and 10. Use the random module
"""

from typing import List
from random import uniform
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async generator function"""
    output = [fun async for fun in async_generator()]
    return output
