# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value

    def printList(self):
        """Print the list values"""
        current = self
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values


def get_smallest_head(headOne, headTwo):
    if headOne.value < headTwo.value:
        return headOne, headTwo
    else:
        return headTwo, headOne


def mergeLinkedLists(headOne, headTwo):
    smallest_head, big_head = get_smallest_head(headOne, headTwo)

    while big_head:
        if smallest_head.next is None:
            smallest_head.next = big_head
            break
        elif big_head.value < smallest_head.next.value:
            pointer_to_next = smallest_head.next
            to_append = big_head
            big_head = big_head.next
            to_append.next = pointer_to_next
            smallest_head.next = to_append
        smallest_head = smallest_head.next
    return get_smallest_head(headOne, headTwo)[0]


if __name__ == "__main__":
    headOne = LinkedList(2, LinkedList(6, LinkedList(7, LinkedList(8))))
    headTwo = LinkedList(1, LinkedList(3, LinkedList(
        4, LinkedList(5, LinkedList(9, LinkedList(10))))))
    result = mergeLinkedLists(headOne, headTwo)
    print(result.printList())
