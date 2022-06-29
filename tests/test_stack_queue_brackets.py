import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_is_valid():
    expected = True
    assert validate_brackets('{}') == expected


def test_strange_is_valid():
    expected = True
    assert validate_brackets('{}(){}') == expected


def test_strange_is_valid_with_keywords():
    expected = True
    assert validate_brackets('()[[Extra Characters]]') == expected


def test_engaged_is_valid():
    expected = True
    assert validate_brackets('(){}[[]]') == expected


def test_engaged_is_valid_keywords():
    expected = True
    assert validate_brackets('{}{Code}[Fellows](())') == expected


def test_is_not_valid():
    expected = False
    assert validate_brackets('[({}]') == expected


def test_is_not_valid_engaged():
    expected = False
    assert validate_brackets('(](') == expected


def test_is_not_valid_2():
    expected = False
    assert validate_brackets('{(})') == expected


def test_is_not_valid_3():
    expected = False
    assert validate_brackets('{(})') == expected


# Edge cases

def test_is_not_valid_edge():
    expected = False
    assert validate_brackets('{') == expected


def test_is_not_valid_edge_2():
    expected = False
    assert validate_brackets(')') == expected


def test_is_not_valid_edge_3():
    expected = False
    assert validate_brackets('[}') == expected
