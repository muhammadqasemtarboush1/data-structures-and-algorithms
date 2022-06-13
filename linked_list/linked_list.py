class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def err_msg(self):
        return "No change, method exception"

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
            elems += "{ " + str(current.value) + " } ->"
            current = current.next
        elems += " NULL"
        return elems

    def include(self, value):
        current = self.head
        while current:
            if current.value == value: return True
            current = current.next
        return False

    def append(self, value):
        '''
         functionally:adds a new node with the given value to the end of the list
        :param new value:
        :return: None
        '''
        current = self.head
        n_node = Node(value)
        if not current:
            current = n_node
        else:
            while current.next:
                current = current.next
            current.next = n_node

    def insert_before(self, s_node, value):
        current = self.head
        n_value = Node(value)
        if not current:
            return self.err_msg()
        elif current.value == s_node:
            self.insert(value)
        else:
            while current.next:
                if current.next.value == s_node:
                    n_value.next = current.next
                    current.next = n_value
                    return
                current = current.next
            return self.err_msg()

    def insert_after(self, s_node, value):
        current = self.head
        n_value = Node(value)
        if not current:
            return self.err_msg()
        elif current.value == s_node:
            n_value.next = self.head
            self.head = n_value
        else:
            while current:
                if current.value == s_node:
                    n_value.next = current.next
                    current.next = n_value
                    break
                current = current.next
            return self.err_msg()

