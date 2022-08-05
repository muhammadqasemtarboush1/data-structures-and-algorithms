class Node:
    """
    Helper class to create node
    """
    def __init__(self, value, next=None):
        """
        Takes two arguments: value =>* , next=> node
        returns: None
        """
        self.value = value
        self.next = next
