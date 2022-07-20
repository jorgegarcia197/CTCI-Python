

# This is the class of the input linked list.


class LinkedList:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def shiftLinkedList(head, k):
    sub_list, count = return_kth_to_last_node(head, k)
    current = sub_list
    while current and current.next:
        current = current.next
    current_from_head = head
    diff = count - k - 1
    current_from_head_head = current_from_head
    for _ in range(diff):
        current_from_head = current_from_head.next
    current_from_head.next = None
    current.next = current_from_head_head
    return sub_list


def shift_ll(head, k):
    head = head
    current = head
    counter = 0
    while current and current.next:
        counter += 1
        current = current.next
    tail = current
    current = head
    offset = abs(k) % counter
    if offset == 0:
        return head
    target = counter - offset if k > 0 else offset

    for i in range(target):
        current = current.next
        new_tail = current
        new_head = current.next
        new_tail.next = None
        tail.next = head
        head = new_head
    return head


def return_kth_to_last_node(head: LinkedList, target: int):
    # This return the kth to the last node of the linked list as a sub-linked-list (because it contains the next values)
    current = head
    count = 0
    # iterate through all the values in the linked list to get the length
    while current and current.next:
        count += 1
        current = current.next
    current.next = head
    # Reset the head
    current = head
    if count < target:
        return
    else:
        for i in range((count-target)+1):
            head = current
            current = current.next
    current.next = None
    return head


if __name__ == "__main__":
    linked_list = LinkedList(0, LinkedList(1, LinkedList(
        2, LinkedList(3, LinkedList(4, LinkedList(5))))))
    output = shift_ll(linked_list, 2)
    while output and output.next:
        print(output.value)
        output = output.next
