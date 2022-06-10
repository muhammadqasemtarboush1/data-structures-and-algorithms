class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    # Adds new node containing 'value' to the first node of the linked list.
    def insert(self, value):
        new_node = Node(value)
        cur = self.head
        if cur != "None":
            self.head = new_node
            new_node.next = cur
        else:
            self.head = new_node


    def to_string(self):
        elems = ''
        current = self.head
        while current:
            elems += "{ " +str(current.value) +" } ->"
            current = current.next
        elems += " NULL"
        return elems

    def include(self, value):
        current = self.head
        while current:
            if current.value == value: return True
            current = current.next
        return False



ll = LinkedList()
ll.insert(5)
ll.insert(7)
ll.insert(12)
ll.insert(0)
print(ll.to_string())