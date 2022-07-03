from trees.binary_tree import *


#
class BinarySearchTree(BinaryTree):

    def add(self, value, node =None):
    #     """
    #         Adds a new node with that value in the correct location in the binary search tree.
    #     """
        pass
    #
    # def contains(self, value, node =None):
    #     """
    #     Argument: value
    #     Returns: boolean indicating whether or not the value is in the tree at least once.
    #     """
        pass

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(20)
    tree.add(340)
    print(tree.contains(20))
    print(tree.contains(100))
    print(tree.root.left.value)