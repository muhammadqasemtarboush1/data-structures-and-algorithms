import pytest
from linked_list.linked_list import Node, LinkedList


#  instantiate an empty linked list
def test_linked_list(ll):
    assert ll


def test_head_value(ll):
    '''
    check the first node is the Head
    Can properly insert into the linked list
    :param ll:
    :return: None
    '''
    actual = ll.head.value
    expected = 0
    assert actual == expected


def test_insert(ll):
    """
  insert into the linked list
  The head property will properly point to the first node in the linked list
    :param ll:
    :return: None
    """
    actual = ll.head.value
    expected = 0
    assert expected == actual



def test_include(ll):
    """
    Will return true when finding a value within the linked list that exists
    :param LinkedList:
    :return: True
    """
    actual = ll.include(7)
    expected = True
    assert actual == expected


def test_not_include(ll):
    """
   Will return false when searching for a value in the linked list that does not exist
    :param LinkedList:
    :return: False
    """
    actual = ll.include(100)
    expected = False
    assert actual == expected


def test_str(ll):
    '''
    return a collection of all the values that exist in the linked list
    '''
    actual = ll.to_string()
    expected = '{ 0 } ->{ 12 } ->{ 7 } ->{ 5 } -> NULL'

    assert actual == expected

def test_insert_multiple(ll):
    """
  insert into the linked list
  The head property will properly point to the first node in the linked list
    :param ll:
    :return: None
    """
    ll.insert(156)
    actual = ll.head.value
    expected = 156
    assert expected == actual
    ll.insert(181)
    actual = ll.head.value
    expected = 181
    assert expected == actual
    ll.insert(109)
    actual = ll.head.value
    expected = 109
    assert expected == actual
    actual = ll.head.value
    ll.insert(1875)
    actual = ll.head.value
    actual = ll.head.value
    expected = 1875
    assert expected == actual



@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(12)
    ll.insert(0)
    return ll
