# Return Kth to Last item in a Linked List

class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value=0, next_value=None):
        self.value = value
        self.next = next_value


def return_kth_to_last_value(head: NodeList, target: int):
    # If we want only the value, we can create an array of values an return the target
    current = head
    values = []
    while current:
        next_value = current.next
        values.append(current.value)
        current = next_value
    diff = (len(values)) - target
    return values[diff] if target < (len(values)) else None


def return_kth_to_last_node(head: NodeList, target: int):
    # This return the kth to the last node of the linked list as a sub-linked-list (because it contains the next values)
    current = head
    count = 0
    # iterate through all the values in the linked list to get the length
    while current:
        count += 1
        current = current.next
    # Reset the head
    current = head
    if count < target:
        return
    else:
        for i in range(count-target):
            current = current.next
    return current

# Extra Problem


def remove_kth_to_last_node(head: NodeList, target: int):
    current = head
    count = 0
    previous = NodeList(0)
    while current:
        count += 1
        current = current.next
    current = head
    if (count-target) == 1:
        head = current.next
    else:
        for i in range((count-target)-1):
            previous = current
            current = current.next
        previous.next = current.next
    return head


if __name__ == "__main__":
    input_linked_list = NodeList(0, NodeList(1, NodeList(2, NodeList(3, NodeList(
        4, NodeList(5, NodeList(6, NodeList(7, NodeList(8, NodeList(9))))))))))
    output = return_kth_to_last_value(input_linked_list, 4)
    print(output)
    # while output:
    #     print(output.value)
    #     output = output.next
