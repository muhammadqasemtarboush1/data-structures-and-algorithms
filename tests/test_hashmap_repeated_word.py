import pytest

from hashtable.repeated_word.text_ex import *
from hashtable.repeated_word.repeated_words import *

def test_normal_str():
    assert repeated_word(case_1) == expected_1


def test_with_capitalize_str():
    assert repeated_word(case_2) == expected_2


def test_with_comma_str():
    assert repeated_word(case_3) == expected_3


def test_no_repeate_str():
    assert repeated_word(case_4) == expected_4
