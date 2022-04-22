""" Singly Linked List """


from SinglyLinkedListNode import NodeList


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        """ Append a new value to the end of the list """
        if self.head is None:
            self.head = NodeList(value)
            self.lenght += 1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = NodeList(value)
        self.length += 1

    def prepend(self, value):
        """ Prepend a new value to the beginning of the list"""
        self.head(value, self.head)
        self.length += 1

    def delete(self, value):
        """ Delete a value from the linked list"""
        # To do this, we need first to check whether te value to delete is the first one
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        else:
            current = self.head
            while current:
                if current.next.value == value:
                    current.next = current.next.next
                    self.length -= 1
                    return

    def reverse(self):
        """ Reverse the linked list"""
        current = self.head
        prev = None
        while current:
            next_value = current.next
            current.next = prev
            prev = current
            current = next_value
        self.head = prev

    def traverseTo(self, index):
        """ Traverse to a given index of the Linked List"""
        current = self.head
        count = 0
        while count != index:
            count += 1
            current = current.next
        return current

    def printList(self):
        """Print the list values"""
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values
