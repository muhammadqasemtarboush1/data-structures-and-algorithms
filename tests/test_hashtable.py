import pytest
from hashtable.hashtable import *


def test_hash_method():
    hash = HashTable()
    expected = 652
    acutal = hash._HashTable__hash('d')

    assert expected == acutal
