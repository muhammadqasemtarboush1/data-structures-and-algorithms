from hashtable.hashtable import *
from trees.binary_tree import *


def add_to_hash(arr):
    hashmap = HashTable()
    for node_val in arr:
        hashmap.set(node_val, str(node_val))
    return hashmap


def check_common(hashmap, arr):
    arr_common = []
    for i in arr:
        if hashmap.contains(i):
            arr_common.append(i)
    return arr_common


def tree_intersection(t1, t2):
    if t1.root is None or t2.root is None:
        return 'no intersection found'
    t1_value = t1.pre_order()
    t2_value = t2.pre_order()

    hash = add_to_hash(t1_value)
    arr_common = check_common(hash, t2_value)

    return arr_common


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree2 = BinaryTree()
    tree2.root = Node(4)
    tree2.root.left = Node(20)
    tree2.root.right = Node(30)
    tree2.root.left.left = Node(33)
    tree2.root.left.right = Node(5)

    print(tree_intersection(tree, tree2))
