from stack_and_queue.stack_and_queue import Queue


def breadth_first(tree):
    if not tree.root:
        return tree.root
    output = []
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        front = queue.dequeue()
        output.append(front.value)

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

    return output
