from trees.binary_tree import *
# from trees.helper_functions.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
             Adds a new node with that value in the correct location in the binary search tree.
        """
        if not self.root:
            self.root = Node(value)
            return
        temp = self.root
        while temp:
            if value > temp.value:
                if not temp.right:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                if not temp.left:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left

    def contains(self, value):
            #     """
            #     Argument: value
            #     Returns: boolean indicating whether or not the value is in the tree at least once.
            #     """
            if not self.root:
                return False
            temp = self.root
            if self.root.value == value:
                return True
            while temp:
                if value > temp.value:

                    if temp.value == value:
                        return True
                    else:
                        if not temp.right:
                            return False
                        temp = temp.right
                else:
                    if temp.value == value:
                        return True
                    else:
                        if not temp.left:
                            return False
                        temp = temp.left
            return  False,"last return"


if __name__ == '__main__':
   tree = BinarySearchTree()
   tree.add(55)
   tree.add(56)
   tree.add(53)
   tree.add(57)
   tree.add(52)
   tree.add(58)
   print(tree.contains(57),'True 57')
   print(tree.contains(52),'True 52')
   print(tree.contains(58),'True 58')
   print(tree.contains(20),'False 20')
   print(tree.contains(80),'False 80')
   print(tree.contains(107),'False 107')
   print(tree.contains(0),'False 0')
   print(tree.contains(1),'False 1')
   print(tree.contains(100000),'False 10000')
   print(tree.pre_order())
   # print(fizz_buzz(tree))
