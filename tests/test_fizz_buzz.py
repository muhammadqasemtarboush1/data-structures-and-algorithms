import pytest
from trees.binary_search_tree import BinarySearchTree
from trees.helper_functions.tree_fizz_buzz.tree_fizz_buzz import *
from trees.helper_functions.b_f_s.b_s_f import breadth_first

# def test_f_b(tree):
#     assert fizz_buzz(tree) == "weeeeeeeeee"

def test_f_b(tree):
    # tree = BinaryTree()
    actual = fizz_buzz(tree)
    expected = breadth_first(tree)
    assert actual == expected

def test_f_b_one_root():
    tree = BinarySearchTree()
    tree.root = Node(5)
    actual = fizz_buzz(tree)
    expected = breadth_first(tree)
    assert actual == expected

def test_f_b_is_empty():
    tree = BinarySearchTree()
    actual = fizz_buzz(tree)
    expected = breadth_first(tree)
    assert actual == expected

@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(15)

    return tree
# [1, 2, 3, 4, 5, 6, 7, 8, 15]

# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'FizzBuzz']