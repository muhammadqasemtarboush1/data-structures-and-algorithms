from stack_and_queue.stack_and_queue import Queue


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


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(50)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(60)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())