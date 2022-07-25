import pytest
from sorting.insertion.insertion import *


def test_insert():
    array = [20, 18, 12, 8, 5, -2]
    assert insertion_sort(array) == [-2, 5, 8, 12, 18, 20]


def test_insert_uniques():
    array = [5, 12, 7, 5, 5, 7]
    assert insertion_sort(array) == [5, 5, 5, 7, 7, 12]


def test_nearly_sorted():
    array = [2, 3, 5, 7, 13, 11]
    assert insertion_sort(array) == [2, 3, 5, 7, 11, 13]


def test_empty():
    array = []
    assert insertion_sort(array) == []
