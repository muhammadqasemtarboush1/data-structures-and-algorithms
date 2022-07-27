import pytest

from sorting.merge.merge import *


def test_merge_sort():
    arr = [8, 4, 23, 42, 16, 15]
    assert merge_sort(arr) == [4, 8, 15, 16, 23, 42]


def test_merge_sort_few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    assert merge_sort(arr) == [5, 5, 5, 7, 7, 12]


def test_merge_sort_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    assert merge_sort(arr) == [2, 3, 5, 7, 11, 13]


def test_merge_sort_sigil_element():
    arr = [2]
    assert merge_sort(arr) == [2]


def test_merge_sort_empty():
    arr = []
    assert merge_sort(arr) == 'please make sure you enter a valid array.'
