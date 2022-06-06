import pytest
from array_binary_search.array_binary_search import binary_search


def test_is_empty():
    actual = binary_search([], 2)
    expected = 'error: invalid input you can not add empty array'
    assert expected == actual
