import pytest
from trees.binary_tree import *
from trees.binary_search_tree import *


# Can successfully instantiate an empty tree
def test_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


# Can successfully instantiate a tree with a single root node
def test_single_root_node():
    tree = BinaryTree()
    tree.root = Node(10)
    actual = tree.root.value
    expected = 10
    assert actual == expected


def test_pre_order(tree):
    actual = tree.pre_order()
    expected = [10, 20, 30, 40, 50, 60]
    assert actual == expected


def test_in_order(tree):
    actual = tree.in_order()
    expected = [30, 20, 40, 10, 60, 50]
    assert actual == expected


def test_post_order(tree):
    actual = tree.post_order()
    expected = [30, 40, 20, 60, 50, 10]
    assert actual == expected


############ BinarySearchTree
# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_to_trees():
    binary_tree = BinarySearchTree()
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    assert binary_tree.root.value == 1


# Can successfully return a collection from a preorder traversal
def test_b_s_trees_preorder():
    binary_tree = BinarySearchTree()
    binary_tree.add(5)
    binary_tree.add(9)
    binary_tree.add(6)
    assert binary_tree.pre_order() == [5, 9, 6]


# Can successfully return a collection from an inorder traversal
def test__b_s_trees_in_order():
    binary_tree = BinarySearchTree()
    binary_tree.add(5)
    binary_tree.add(9)
    binary_tree.add(6)
    assert binary_tree.in_order() == [5, 6, 9]


# Can successfully return a collection from a postorder traversal
def test_b_s_trees_post_order():
    binary_tree = BinarySearchTree()
    binary_tree.add(5)
    binary_tree.add(9)
    binary_tree.add(6)
    assert binary_tree.post_order() == [6, 9, 5]


# Returns true	false for the contains method, given an existing
def test_contain_true():
    binary_tree = BinarySearchTree()
    binary_tree.add(5)
    binary_tree.add(9)
    binary_tree.add(6)
    assert binary_tree.contains(5) == True


def test_contain_false():
    binary_tree = BinarySearchTree()
    binary_tree.add(5)
    binary_tree.add(9)
    binary_tree.add(6)
    assert binary_tree.contains(55) == False


def test_max_in_empty_tree():
    binary_tree = BinarySearchTree()
    assert binary_tree.max_in_tree() == "There is no item in this tree"

def test_max_in_tree(tree):
    # binary_tree = BinarySearchTree()
    assert tree.max_in_tree() == 60

def test_max_in_tree_new_tree():
    binary_tree = BinarySearchTree()
    binary_tree.root = Node(56)
    binary_tree.root.left = Node(1)
    binary_tree.root.right = Node(9)
    binary_tree.root.left.left = Node(0)
    binary_tree.root.left.right = Node(100)
    assert binary_tree.max_in_tree() == 100



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
