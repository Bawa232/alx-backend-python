#!/usr/bin/env python3
''' complex types '''

from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple:
    ''' fn that returns a tuple of str and f/int '''

    return (k, float(v**2)
