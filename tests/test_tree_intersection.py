import pytest
from trees.binary_search_tree import *
from hashtable.tree_intersection.tree_intersection import *


def test_happy_path(tree, tree2):
    assert tree_intersection(tree, tree2) == [60, 50]


def test_empty_tree(tree2):
    t1 = BinaryTree()
    assert tree_intersection(t1, tree2) == 'no intersection found'


def test_no_match(tree2):
    t1 = BinaryTree()
    tree.root = Node(110)
    tree.root.left = Node(120)
    tree.root.right = Node(520)
    tree.root.left.left = Node(230)
    tree.root.left.right = Node(420)
    assert tree_intersection(t1, tree2) == 'no intersection found'


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


@pytest.fixture
def tree2():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(0)
    tree.root.right = Node(50)
    tree.root.left.left = Node(300)
    tree.root.left.right = Node(60)
    tree.root.right.left = Node(70)
    return tree
