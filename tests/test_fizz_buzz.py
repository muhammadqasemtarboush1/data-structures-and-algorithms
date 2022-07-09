import pytest
from trees.binary_tree import *
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
    tree = BinaryTree()
    tree.root = Node(5)
    actual = fizz_buzz(tree)
    expected = breadth_first(tree)
    assert actual == expected

def test_f_b_is_empty():
    tree = BinaryTree()
    actual = fizz_buzz(tree)
    expected = breadth_first(tree)
    assert actual == expected

@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(6)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(8)
    tree.root.right.right.left = Node(15)
    return tree
# [1, 2, 3, 4, 5, 6, 7, 8, 15]

# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'FizzBuzz']