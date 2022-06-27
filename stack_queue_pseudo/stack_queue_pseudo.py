from stack_and_queue.stack_and_queue import Stack
class EmptyQueueException(Exception):
    pass


class PseudoQueue:
    def __init__(self):
        self.pseudo_queue = Stack()
        self.pseudo_queue_2 = Stack()

    def enqueue(self, value):
        '''
        Arguments: value
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
       '''
        self.pseudo_queue.push(value)

    def dequeue(self):
        '''
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
       '''
        if self.pseudo_queue.is_empty():
            print("emptyyyyyyyyyyyyyyyyyyyy")
            raise EmptyQueueException('Empty Queue')

        while not self.pseudo_queue.is_empty():
            popped = self.pseudo_queue.pop()
            self.pseudo_queue_2.push(popped)
        dequed = self.pseudo_queue_2.pop()
        while not self.pseudo_queue_2.is_empty():
            popped = self.pseudo_queue_2.pop()
            self.pseudo_queue.push(popped)
        return dequed

    def __str__(self):
        current = self.pseudo_queue.top
        items = ''
        while current:
            items += str(current.value) + ' -> '
            current = current.next

        return items


if __name__ == '__main__':
    fake_queue = PseudoQueue()
    fake_queue.enqueue(1)
    fake_queue.enqueue(2)
    fake_queue.enqueue(3)
    fake_queue.enqueue(4)
    fake_queue.enqueue(20)
    print(fake_queue.__str__())
