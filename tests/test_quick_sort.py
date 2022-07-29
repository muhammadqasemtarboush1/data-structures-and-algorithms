import pytest
from sorting.quick.quick import *


def test_quick_sort():
    array = [8, 4, 23, 42, 16, 15]
    assert quick_sort(array, 0, len(array) - 1) == [4, 8, 15, 16, 23, 42]


def test_quick_sort_reverse_sorted():
    array = [20, 18, 12, 8, 5, -2]
    assert quick_sort(array, 0, len(array) - 1) == [-2, 5, 8, 12, 18, 20]


def test_quick_sort_few_uniques():
    array = [5, 12, 7, 5, 5, 7]
    assert quick_sort(array, 0, len(array) - 1) == [5, 5, 5, 7, 7, 12]


def test_quick_sort_nearly_sorted():
    array = [2, 3, 5, 7, 13, 11]
    assert quick_sort(array, 0, len(array) - 1) == [2, 3, 5, 7, 11, 13]


def test_quick_sort_empty():
    array = []
    assert quick_sort(array, 0, len(array) - 1) == []


def test_quick_sort_single():
    array = [2]
    assert quick_sort(array, 0, len(array) - 1) == [2]
