#!/usr/bin/env python3
''' python asyn/await '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' returns a random float '''
    w_time = random.random() * max_delay
    await asyncio.sleep(w_time)
    return w_time
