class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):

        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):

        if not self.top:
            raise EmptyStackException("Nothing to pop ,Empty Stack")

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):

        return True if self.top is None else False

    def peek(self):

        if self.is_empty() == False:
            return self.top.value
        else:
            raise EmptyStackException("No peek, Empty Stack")

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + ' - '
            current = current.next

        return items


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def is_empty(self):
        return True if self.front is None else False

    def peek(self):
        if self.is_empty():
            raise EmptyQueueException('Empty Queue')
        else:
            return self.front.value

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException('Queue Empty')
        else:
            dequeued = self.front
            self.front = self.front.next
        return dequeued.value

    def __str__(self):
        current = self.front
        items = ''
        while current:
            items += str(current.value) + ' - '
            current = current.next

        return items

#
# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.is_empty())
#     queue = Queue()
#     print(stack.is_empty())
