from trees.helper_functions.tree_fizz_buzz.k_tree import *


def fizz_buzz(tree):
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
                output.append(str(front.value))
            # counter=0
            # if front.children[counter]
            #   queue.enqueue[front.children[counter]
            #   counter+=1
            for i in front.children:
                queue.enqueue(i)

    return output
