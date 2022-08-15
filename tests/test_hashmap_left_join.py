import pytest
from hashtable.hashtable import *
from hashtable.hashmap_left_join.hashmap_left_join import hash_left_join


def test_happy_path(hash_1, hash_2):
    assert hash_left_join(hash_1, hash_2) == {'fond': {'averse', 'fond', 'enamored'},
                                              'guide': {'follow', 'guide', 'usher'},
                                              'outfit': {'garb', 'No_match', 'outfit'},
                                              'wrath': {'wrath', 'anger', 'delight'}}


@pytest.fixture
def hash_1():
    h1 = HashTable()
    h1.set('fond', 'enamored')
    h1.set('guide', 'usher')
    h1.set('outfit', 'garb')
    h1.set('wrath', 'anger')
    return h1


@pytest.fixture
def hash_2():
    h2 = HashTable()
    h2.set('fond', 'averse')
    h2.set('guide', 'follow')
    h2.set('flow', 'jam')
    h2.set('wrath', 'delight')
    return h2

# {'fond': {'averse', 'fond', 'enamored'}, 'guide': {'follow', 'guide', 'usher'}, 'outfit': {'garb', 'No_match',
# 'outfit'}, 'wrath': {'wrath', 'anger', 'delight'}}
