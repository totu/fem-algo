#!/usr/bin/env python3
def linear_search(haystack: list[int], needle: int) -> bool:
    for hay in haystack:
        if hay == needle:
            return True
    return False


def test_linear_search():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_search(foo, 69)
    assert not linear_search(foo, 1336)
    assert linear_search(foo, 69420)
    assert not linear_search(foo, 69421)
    assert linear_search(foo, 1)
    assert not linear_search(foo, 0)
