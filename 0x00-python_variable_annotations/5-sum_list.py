#!/usr/bin/env python3
''' complex types '''


def sum_list(input_list: list[float]) -> float:
    ''' fn that sums fkoats in a list '''
    add: float = 0
    for num in input_list:
        add += num

    return add
