

class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value=0, next_value=None):
        self.value = value
        self.next = next_value


def remove_dups(head: NodeList):
    ## This is a O(n) space and time complexity
    seen = []
    current = head
    previous = NodeList()
    while current:
        next_value = current.next
        if current.value in seen:
            previous.next = current.next
        else:
            seen.append(current.value)
            previous = current
        current = next_value
    return head


def remove_dups_no_buffer(head: NodeList):
    # This means we don't have the seen list, instead we have to do a or a runner method
    # A runner method consist on a slow and fast pointer 
    # this becomes a o(n^2) Time Complexity but O(1) space
    first_pointer = head
    previous = NodeList()
    while first_pointer:
        second_pointer = first_pointer.next
        while second_pointer:
            if first_pointer.value == second_pointer.value:
                previous.next = second_pointer.next
            else:
                previous = second_pointer
            second_pointer = second_pointer.next
        first_pointer = first_pointer.next
    return head


if __name__ == "__main__":
    myLinkedList = NodeList(2, NodeList(3, NodeList(4, NodeList(
        10, NodeList(11, NodeList(3, NodeList(1, NodeList(0))))))))
    output = remove_dups(myLinkedList)
    output2 = remove_dups_no_buffer(myLinkedList)
