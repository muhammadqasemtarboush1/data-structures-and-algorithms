def zip_lists(link_1, link_2):
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
