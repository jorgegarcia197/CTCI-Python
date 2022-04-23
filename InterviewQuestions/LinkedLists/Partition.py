# 2.4 Partition of a linked list


class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def partition(head, partition):
    left = left_head = NodeList(0)
    right = right_head = NodeList(0)
    current = head
    while current:
        if current.value < partition:
            # we append it to the left linked_list
            left.next = current
            left = left.next
        else:
            # we append it to the right linked_list
            right.next = current
            right = right.next
        # We update the current to the next to keep the loop going
        current = current.next
    right.next = None  # we point the last node to None
    # Since we initialized a Node of value 0, we get the next and connect it to the left linked list
    left.next = right_head.next
    return left_head.next

