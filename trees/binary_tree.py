from trees.helper_functions.b_s_f import breadth_first


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):

        self.root = None

    def def_act(self, value, arr=None):

        arr = arr or []
        arr.append(value)
        return arr

    def pre_order(self, node=None, temp_act=None, stored_value=None):
        temp_act = temp_act or self.def_act
        if not self.root:
            return temp_act()
        node = node or self.root
        stored_value = temp_act(node.value, stored_value)
        if node.left:
            stored_value = self.pre_order(node.left, temp_act, stored_value)
        if node.right:
            stored_value = self.pre_order(node.right, temp_act, stored_value)
        return stored_value

    def post_order(self, node=None, temp_act=None, stored_value=None):
        temp_act = temp_act or self.def_act
        if not self.root:
            return temp_act()
        node = node or self.root
        if node.left:
            stored_value = self.post_order(node.left, temp_act, stored_value)
        if node.right:
            stored_value = self.post_order(node.right, temp_act, stored_value)
        stored_value = temp_act(node.value, stored_value)
        return stored_value

    def in_order(self, node=None, temp_act=None, stored_value=None):
        if temp_act is None:
            temp_act = self.def_act
        if not self.root:
            return temp_act()
        node = node or self.root
        if node.left:
            stored_value = self.in_order(node.left, temp_act, stored_value)
        stored_value = temp_act(node.value, stored_value)
        if node.right:
            stored_value = self.in_order(node.right, temp_act, stored_value)
        return stored_value

    def max_in_tree(self):
        '''
        deal with numeric values and return the max value
        :return: max value in tree
        '''

        if not self.root:
            return 'There is no item in this tree'
        # max = self.root.value
        tree = self.pre_order()
        max = tree[0]
        for i in tree:
            if i > max:
                max = i
        return max

    # while temp.value:
    #     if max > temp.value:
    #
    #         if temp.value == max:
    #             # return True
    #             max = temp.value
    #             print(max,'in first else')
    #
    #         else:
    #             if not temp.right:
    #                 return False
    #             temp = temp.right
    #             print(max,'in lasr else')
    #
    #     else:
    #         if temp.value == max:
    #             # return True
    #             max = temp.value
    #             print(max,'in lasr else')
    #         # else:
    #         #     # if not temp.left:
    #         #     # return False
    #             temp = temp.left
    # return max


if __name__ == "__main__":
    tree = BinaryTree()
    # tree.root = Node(10)
    # tree.root.left = Node(20)
    # tree.root.right = Node(50)
    # tree.root.left.left = Node(30)
    # tree.root.left.right = Node(40)
    # # [10, 20, 30, 40, 50, 60]
    # tree.root.right.left = Node(60)
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    # print(tree.max_in_tree())
    # print(breadth_first(tree))
# [2, 7, 5, 2, 6, 9, 5, 11, 4]
    tree.root = Node(2)
    # tree.root.left = Node(7)
    # tree.root.right = Node(5)
    # tree.root.left.left = Node(2)
    # tree.root.left.right = Node(6)
    # # [10, 20, 30, 40, 50, 60]
    # tree.root.right.right = Node(9)
    # tree.root.left.right.left = Node(5)
    # tree.root.left.right.right = Node(11)
    # tree.root.right.right.left = Node(4)

    print(breadth_first(tree))

