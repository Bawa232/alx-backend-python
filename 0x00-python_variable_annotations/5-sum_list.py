#!/usr/bin/env python3
''' complex types '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' fn that sums fkoats in a list '''
    add = 0
    for num in input_list:
        add += num

    return add
