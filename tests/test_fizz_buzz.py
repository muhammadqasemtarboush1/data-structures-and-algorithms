import pytest
from trees.binary_search_tree import *
from trees.helper_functions.tree_fizz_buzz.tree_fizz_buzz import *
from trees.helper_functions.b_f_s.b_s_f import breadth_first

# def test_f_b(tree):
#     assert fizz_buzz(tree) == "weeeeeeeeee"

def test_f_b(tree):
    # tree = BinaryTree()
    actual = fizz_buzz(tree)
    expected = ['1', '2', 'Fizz', '4', 'Buzz','Fizz', '7', '8', 'FizzBuzz']
    assert actual == expected

def test_f_b_one_root():
    tree = BinaryTree()
    tree.root = Node(5)
    actual = fizz_buzz(tree)
    expected = ['Buzz']
    assert actual == expected

def test_f_b_is_empty():
    tree = BinaryTree()
    actual = fizz_buzz(tree)
    expected = 'No root for this tree'
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
    tree.add(15)
    # tree = BinaryTree()
    # tree.root = Node(2)
    # tree.root.left = Node(7)
    # tree.root.right = Node(5)
    # tree.root.left.left = Node(2)
    # tree.root.left.right = Node(6)
    # tree.root.right.right = Node(9)
    # tree.root.left.right.left = Node(5)
    # tree.root.left.right.right = Node(11)
    # tree.root.right.right.left = Node(4)

    return tree
# [1, 2, 3, 4, 5, 6, 7, 8, 15]

# ['1', '2', 'Fizz', '4', 'Buzz', '7', '8', 'Fizz', 'FizzBuzz']