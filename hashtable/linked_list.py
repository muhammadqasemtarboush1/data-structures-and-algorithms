from hashtable.node import *


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Instantiates a singly-linked list with an empty head node.
        Args: head (None by default)
        Outputs: None
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
        arguments :
        value
        returns:
        None
        """
        node = Node(value)
        node.next = self.head
        self.head = node
