import pytest
from linked_list.linked_list import LinkedList
from linked_list.zip_list.zip_list import zip_lists

def test_zip_listes(ll_one, ll_two):
    actual = zip_lists(ll_one,ll_two).to_string()
    expected = '{ 1 } ->{ 5 } ->{ 3 } ->{ 9 } ->{ 2 } ->{ 4 } -> NULL'
    assert expected == actual


def test_zip_liste_len1_more_len2(ll_one, ll_two):
    ll_one.insert(6)
    # print(zip_lists(ll_one,ll_two).to_string())
    actual = zip_lists(ll_one,ll_two).to_string()
    expected = '{ 6 } ->{ 5 } ->{ 1 } ->{ 9 } ->{ 3 } ->{ 4 } ->{ 2 } -> NULL'
    assert expected == actual


def test_zip_liste_len1_less_len2(ll_one, ll_two):
    ll_two.insert(6)
    actual = zip_lists(ll_one,ll_two).to_string()
    expected = '{ 1 } ->{ 6 } ->{ 3 } ->{ 5 } ->{ 2 } ->{ 9 } ->{ 4 } -> NULL'
    assert expected == actual


@pytest.fixture
def ll_one():
    ll_one = LinkedList()
    ll_one.insert(2)
    ll_one.insert(3)
    ll_one.insert(1)
    return ll_one

@pytest.fixture
def ll_two():
    ll_two = LinkedList()
    ll_two.insert(4)
    ll_two.insert(9)
    ll_two.insert(5)
    return ll_two
