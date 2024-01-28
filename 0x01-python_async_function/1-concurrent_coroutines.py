#!/usr/bin/env python3
''' python async programming '''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' returns delay times '''
    lis_t = []
    i = 0

    while i < n:
        list_t.append(wait_random(max_delay))
        i += 1

    return sorted(list_t)
