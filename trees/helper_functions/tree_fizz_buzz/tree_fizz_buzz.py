from stack_and_queue.stack_and_queue import *
from trees.binary_search_tree import *
def fizz_buzz (tree):
    '''
    Write a function called fizz buzz tree
    Arguments: k-ary tree
    Return: new k-ary tree
    '''
    if not tree.root:
        return "No root for this tree"
    output = BinarySearchTree()
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        front = queue.dequeue()
        if front.value:
            if front.value % 3 == 0 and front.value % 5 == 0:
                output.add('FizzBuzz')
            elif front.value % 3 == 0:
                output.add('Fizz')
            elif front.value % 5 == 0:
                output.add('Buzz')
            else:
                output.add(str(front.value))
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)

    return output

if __name__ == "__main__":
    tree = BinarySearchTree()
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
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # [10, 20, 30, 40, 50, 60]
    tree.root.right.right = Node(6)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(8)
    tree.root.right.right.left = Node(15)

    print(breadth_first(tree))
    tree =fizz_buzz(tree)
    print(tree.pre_order())

