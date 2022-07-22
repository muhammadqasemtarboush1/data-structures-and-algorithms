from stack_and_queue.stack_and_queue import *


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class KT:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return self.root
        c_output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            c_output.append(front.value)

            for child in front.children:
                queue.enqueue(child)

        return c_output



# KT code from stack overflow