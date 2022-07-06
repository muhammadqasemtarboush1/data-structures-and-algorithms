import pytest
# from stack_and_queue.stack_and_queue import Queue
from trees.binary_tree import *
from trees.helper_functions.b_s_f import *


def test_bsf(tree):
    assert breadth_first(tree) == [10, 20, 50, 30, 40, 60]


def test_bsf_in_empty():
    tree = BinaryTree()
    assert breadth_first(tree) == 'No root for this tree'

def test_bsf_one_root():
    tree = BinaryTree()
    tree.root = Node(5)
    assert breadth_first(tree) == [5]


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
