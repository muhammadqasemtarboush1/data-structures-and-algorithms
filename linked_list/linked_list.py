class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def err_msg(self,err):
        if err == 1:
            return "No change, method exception"
        if err == 2:
            return "Exception error value not found"
        else:
            return "Negative value not expected"

    # Adds new node containing 'value' to the first node of the linked list.
    def insert(self, value):
        new_node = Node(value)
        cur = self.head
        if cur != "None":
            self.head = new_node
            new_node.next = cur
            self.length += 1
        else:
            self.head = new_node
            self.length += 1

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
            self.length += 1
        else:
            while current.next:
                current = current.next
            self.length += 1
            current.next = n_node


    def insert_before(self, s_node, value):
        current = self.head
        n_value = Node(value)
        if not current:
            return self.err_msg(1)
        elif current.value == s_node:
            self.insert(value)
        else:
            while current.next:
                if current.next.value == s_node:
                    n_value.next = current.next
                    current.next = n_value
                    break
                current = current.next
            self.length += 1
            return self.err_msg(1)

    def insert_after(self, s_node, value):
        current = self.head
        n_value = Node(value)
        if not current:
            return self.err_msg(1)
        elif current.value == s_node:
            n_value.next = self.head
            self.head = n_value
            self.length += 1
        else:
            while current:
                if current.value == s_node:
                    n_value.next = current.next
                    current.next = n_value
                    self.length += 1
                    break
                current = current.next
            return self.err_msg(1)

    def kth_form_end(self, k):
        #     '''
        #     :param self:
        #     :param k:
        #     :return:Return the node’s value that is k places from the tail of the linked list.
        #     '''

            last_node = current = self.head
            counter = 0
            if self.length < k or self.length == 0:
                return self.err_msg(2)
            if k < 0:
                return self.err_msg(3)
            while last_node:
                if counter > k:
                    current = current.next
                else:
                    current = current
                last_node = last_node.next
                counter += 1
            if counter > k:
                return current.value



    def zip_lists(self,link_1, link_2):
        '''
        Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
        :param: 2 linked lists
        :return: Linked List, zipped
        '''
        link_1_current = link_1.head
        link_1_previous = link_1_current
        link_2_current = link_2.head
        link_2_previous = link_2_current
        while link_1_current or link_2_current:
            if link_1_current:
                link_1_previous = link_1_current
                link_1_current = link_1_current.next

            if link_2_current:
                link_2_previous = link_2_current
                link_2_current = link_2_current.next
                link_2_previous.next = link_1_current
                link_1_previous.next = link_1_previous = link_2_previous
        return link_1

if __name__ == "__main__":

    link_1 = LinkedList()
    # link_1.insert(2)
    link_1.insert(3)
    link_1.insert(1)
    link_2 = LinkedList()
    link_2.insert(4)
    link_2.insert(9)
    link_2.insert(5)
    listvalue = link_1.zip_lists(link_1,link_2)
    print(listvalue.to_string())


