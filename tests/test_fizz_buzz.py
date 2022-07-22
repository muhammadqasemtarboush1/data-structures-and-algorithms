import pytest
from trees.helper_functions.tree_fizz_buzz.tree_fizz_buzz import *


# from trees.helper_functions.b_f_s.b_s_f import breadth_first

# def test_f_b(tree):
#     assert fizz_buzz(tree) == "weeeeeeeeee"

def test_f_b(tree):
    # tree = BinaryTree()
    actual = fizz_buzz(tree)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', '7', 'Fizz', 'FizzBuzz']
    assert actual == expected


def test_f_b_one_root():
    tree = KT()
    tree.root = Node(5)
    actual = fizz_buzz(tree)
    expected = ['Buzz']
    assert actual == expected


def test_f_b_chek_if_match_root(tree):
    actual = tree.breadth_first()
    expected = [1, 2, 3, 4, 5, 7, 9, 15]
    assert actual == expected


def test_f_b_is_empty():
    tree = KT()
    actual = fizz_buzz(tree)
    expected = 'No root for this tree'
    assert actual == expected


@pytest.fixture
def tree():
    tree = KT()
    tree.root = Node(1)
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(3))
    tree.root.children[0].children.append(Node(4))
    tree.root.children[1].children.append(Node(5))
    tree.root.children[1].children.append(Node(7))
    tree.root.children[1].children[0].children.append(Node(9))
    tree.root.children[1].children[1].children.append(Node(15))
    # ['1', '2', 'Fizz', '4', 'Buzz', '7', 'Fizz', 'FizzBuzz']
    return tree
