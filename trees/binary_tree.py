from stack_and_queue.stack_and_queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def default_action(self, value, arr=None):
        arr = arr or []
        arr.append(value)
        return arr

    def pre_order(self, node=None, action=None, acc=None):
        action = action or self.default_action
        if not self.root:
            return action()
        node = node or self.root
        acc = action(node.value, acc)
        if node.left:
            acc = self.pre_order(node.left, action, acc)
        if node.right:
            acc = self.pre_order(node.right, action, acc)
        return acc

    def in_order(self, node=None, action=None, acc=None):
        if action is None:
            action = self.default_action
        if not self.root:
            return action()
        node = node or self.root
        if node.left:
            acc = self.in_order(node.left, action, acc)
        acc = action(node.value, acc)
        if node.right:
            acc = self.in_order(node.right, action, acc)
        return acc

    def post_order(self, node=None, action=None, acc=None):
        action = action or self.default_action
        if not self.root:
            return action()
        node = node or self.root
        if node.left:
            acc = self.post_order(node.left, action, acc)
        if node.right:
            acc = self.post_order(node.right, action, acc)
        acc = action(node.value, acc)
        return acc


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(50)
    tree.root.left.left = Node(30)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(60)
    # print(tree.breadth_first())
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())

    # print("+++++++++++++++++")
    # tree.pre_order_iter()
