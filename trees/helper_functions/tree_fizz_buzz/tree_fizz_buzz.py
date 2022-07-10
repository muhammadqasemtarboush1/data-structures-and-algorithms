from trees.binary_search_tree import *
from stack_and_queue.stack_and_queue import *

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
                output.add(str(front.value) + ' Fizz')
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
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(15)
    print(tree.pre_order())
    tree = fizz_buzz(tree)
    print(tree.pre_order())
# ['1', '2', '3 Fizz', '4', 'Buzz', '6 Fizz', '7', '8', '9 Fizz', 'FizzBuzz']
