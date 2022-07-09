import pytest
from trees.binary_tree import *
from trees.helper_functions.tree_fizz_buzz.tree_fizz_buzz import *


def test_f_b(tree):
    assert fizz_buzz(tree) # some test


def test_f_b_in_empty():
    tree = BinaryTree()
    assert fizz_buzz(tree) == 'No root for this tree'

def test_f_b_one_root():
    tree = BinaryTree()
    tree.root = Node(5)
    assert fizz_buzz(tree)# some test


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(50)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(60)
    return tree
