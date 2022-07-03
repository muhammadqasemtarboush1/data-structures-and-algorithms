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
    actual =tree.root.value
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
    expected =[30, 40, 20, 60, 50, 10]
    assert actual == expected




############ BinarySearchTree
# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_to_trees():
  binary_tree=BinarySearchTree()
  binary_tree.add(1)
  binary_tree.add(2)
  binary_tree.add(3)
  assert binary_tree.root.value == 1

# Can successfully return a collection from a preorder traversal

# Can successfully return a collection from an inorder traversal

# Can successfully return a collection from a postorder traversal

# Returns true	false for the contains method, given an existing




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

# @pytest.fixture
# def tree():
#   return BinaryTree()
