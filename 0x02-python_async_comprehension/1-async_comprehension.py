#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""

from typing import List
from random import uniform
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension"""
    output = [fun async for fun in async_generator()]
    return output
