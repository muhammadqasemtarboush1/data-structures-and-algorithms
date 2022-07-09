from stack_and_queue.stack_and_queue import *

def fizz_buzz (tree):
    '''
    Write a function called fizz buzz tree
    Arguments: k-ary tree
    Return: new k-ary tree
    '''
    if not tree.root:
        return "No root for this tree"
    output = []
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        front = queue.dequeue()
        if front.value:
            if front.value % 3 == 0 and front.value % 5 == 0:
                output.append('FizzBuzz')
            elif front.value % 3 == 0:
                output.append('Fizz')
            elif front.value % 5 == 0:
                output.append('Buzz')
            else:
                output.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)

    return output
