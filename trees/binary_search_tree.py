from trees.binary_tree import *


#
class BinarySearchTree(BinaryTree):

    # def add(self, value, node =None):
    #     """
    #         Adds a new node with that value in the correct location in the binary search tree.
    #     """
    #     pass
    #
    # def contains(self, value, node =None):
    #     """
    #     Argument: value
    #     Returns: boolean indicating whether or not the value is in the tree at least once.
    #     """
    #     pass
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur_node = self.root
        added_to_tree = False
        while not added_to_tree:
            if cur_node.value >= value:
                if cur_node.left is None:
                    cur_node.left = Node(value)
                    added_to_tree = True
                else:
                    cur_node = cur_node.left
            elif cur_node.value < value:
                if cur_node.right is None:
                    cur_node.right = Node(value)
                    added_to_tree = True
                else:
                    cur_node = cur_node.right

    def contains(self, value):
        bool_res = False
        cur_node = self.root
        while not bool_res:
            if cur_node.value == value:
                return True
            elif cur_node.value > value:
                if cur_node.left is None:
                    bool_res = True
                else:
                    cur_node = cur_node.left
            elif cur_node.value < value:
                if cur_node.right is None:
                    bool_res = True
                else:
                    cur_node = cur_node.right
        return False

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(20)
    tree.add(340)
    print(tree.contains(20))
    print(tree.contains(100))
    print(tree.root.left.value)