import pytest
from linked_list.linked_list import LinkedList
from linked_list.zip_list.zip_list import zip_lists

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


# Can successfully add a node to the end of the linked list
def test_append(ll):
    ll.append(55)
    actual = ll.to_string()
    expected = '{ 0 } ->{ 12 } ->{ 7 } ->{ 5 } ->{ 55 } -> NULL'
    assert actual == expected


# Can successfully add multiple nodes to the end of a linked list
def test_append_multiple(ll):
    ll.append(55)
    ll.append(85)
    ll.append(65)
    actual = ll.to_string()
    expected = '{ 0 } ->{ 12 } ->{ 7 } ->{ 5 } ->{ 55 } ->{ 85 } ->{ 65 } -> NULL'
    assert actual == expected


# Can successfully insert a node before the first node of a linked list
def test_insert_before(linked_insert):
    linked_insert.insert_before(1, 5)
    actual = linked_insert.to_string()
    expected = "{ 5 } ->{ 1 } ->{ 3 } ->{ 2 } -> NULL"
    assert expected == actual


# Can successfully insert a node before a node located i the middle of a linked list
def test_insert_before_middle(linked_insert):
    linked_insert.insert_before(3, 5)
    actual = linked_insert.to_string()
    expected = "{ 1 } ->{ 5 } ->{ 3 } ->{ 2 } -> NULL"
    assert expected == actual


# Can successfully insert after a node in the middle of the linked list
def test_insert_after_middle_node(linked_insert):
    linked_insert.insert_after(3, 5)
    actual = linked_insert.to_string()
    expected = "{ 1 } ->{ 3 } ->{ 5 } ->{ 2 } -> NULL"
    assert expected == actual


# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node(linked_insert):
    linked_insert.insert_after(2, 5)
    actual = linked_insert.to_string()
    expected = "{ 1 } ->{ 3 } ->{ 2 } ->{ 5 } -> NULL"
    assert expected == actual


def test_kth_in_lingth(ll):
    pass


def test_kth_out_range(ll):
    # Where k is greater than the length of the linked list
    actual = ll.kth_form_end(11)
    expected = 'Exception error value not found'
    assert expected == actual


def test_kth_in_range(ll):
    # Where k and the length of the list are the same
    actual = ll.kth_form_end(3)
    print(ll.to_string())
    print(ll.length)
    expected = '0'
    assert expected == str(actual)


def test_kth_positive(ll):
    # Where k is not a positive integer
    actual = ll.kth_form_end(-1)
    expected = 'Negative value not expected'
    assert expected == actual


def test_kth_size1(ll_size1):
    # Where the linked list is of a size 1
    actual = ll_size1.kth_form_end(0)
    expected = "5"
    assert expected == str(actual)


def test_kth_in_middle(ll):
    # Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    actual = ll.kth_form_end(2)
    expected = "12"
    assert expected == str(actual)


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(12)
    ll.insert(0)
    return ll


@pytest.fixture
def linked_insert():
    newlink = LinkedList()
    newlink.insert(2)
    newlink.insert(3)
    newlink.insert(1)
    return newlink


@pytest.fixture
def ll_size1():
    ll_size1 = LinkedList()
    ll_size1.insert(5)
    return ll_size1


