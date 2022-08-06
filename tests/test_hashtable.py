import pytest
from hashtable.hashtable import *


def test_hash_method(hash):
    assert hash._HashTable__hash('d') == 0


# Setting a key/value to your hashtable results in the value being in the data structure
def test_hash_method_set(hash):
    assert '84' == hash.get('d')


# Retrieving based on a key returns the value stored
def test_hash_method_get(hash):
    assert "8" == hash.get('f')


# Successfully returns null for a key that does not exist in the hashtable
def test_hash_method_not_found(hash):
    assert None == hash.get('q')


# Successfully returns a list of all unique keys that exist in the hashtable
def test_hash_method_list_of_keys(hash):
    assert ['d', 'f', 't'] == hash.key()


# Successfully handle a collision within the hashtable
def test_hash_method_collision(hash):
    hash.set('tan 1', '1')
    hash.set('tan 2', '2')
    hash.set('tan 3', '3')
    hash.set('tan 4', '4')
    hash.set('tan 5', '5')
    hash.set('tan 6', '6')
    hash.set('tan 7', '7')
    hash.set('tan 8', '8')
    hash.set('tan 9', '9')
    hash.set('tan 10', '10')
    hash.set('tan 0', '0')
    assert "0" == hash.get('tan 0')


# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_hash_method_return_value_with_collision(hash):
    hash.set('tan 1', '1')
    hash.set('tan 2', '2')
    hash.set('tan 3', '3')
    hash.set('tan 4', '4')
    hash.set('tan 5', '5')
    hash.set('tan 6', '6')
    hash.set('tan 7', '7')
    hash.set('tan 8', '8')
    hash.set('tan 9', '9')
    hash.set('tan 10', '10')
    hash.set('tan 0', '0')
    assert "0" == hash.get('tan 0')
    assert "2" == hash.get('tan 2')
    assert "5" == hash.get('tan 5')
    assert "6" == hash.get('tan 6')
    assert "8" == hash.get('tan 8')


# Successfully hash a key to an in-range value
def test_hash_method_hash_in_range(hash):
    assert hash._HashTable__hash('statement ') == 9

@pytest.fixture
def hash():
    hash = HashTable()
    hash.set('d', '84')
    hash.set('f', '8')
    hash.set('t', '4')
    return hash
