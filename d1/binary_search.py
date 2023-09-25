#!/usr/bin/env python3
import math


def binary_search(haystack: list[int], needle: [int]) -> bool:
    low = 0
    high = len(haystack)

    while high > low:
        mid = math.floor(low + (high - low) / 2)
        value = haystack[mid]

        if value == needle:
            return True
        elif value > needle:
            high = mid
        else:
            low = mid + 1

    return False


def test_binary_search():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search(foo, 69)
    assert not binary_search(foo, 1336)
    assert binary_search(foo, 69420)
    assert not binary_search(foo, 69421)
    assert binary_search(foo, 1)
    assert not binary_search(foo, 0)
