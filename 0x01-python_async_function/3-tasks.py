#!/usr/bin/env python3
"""
Normal function that creates async task
"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a task"""
    return asyncio.create_task(wait_random(max_delay))
