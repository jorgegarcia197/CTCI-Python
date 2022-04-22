""" Singly Linked List """

from SinglyLinkedListNode import NodeList


class SinglyLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0
        if value:
            self.append(value)

    def append(self, value):
        """Append a new value to the end  Double Linked List

        Args:
            value (int): The value that would hold the new node

        Returns:
            List: The list of values after the appending
        """
        newNode = NodeList(value)
        if self.tail:
            self.tail.next = newNode
        self.tail = newNode
        if not self.head:
            self.head = newNode
        self.length += 1
        return self.printList()

    def prepend(self, value):
        """Add a new value at the beginning of the linked list, replacing the head value with the new value

        Args:
            value (int): the value that would hold the new head
        """
        self.head = NodeList(value, self.head)
        self.length += 1

    def deletebyValue(self, value):
        """Deletes the first instance of the value passed in the parameter

        Args:
            value (int): the value of the node that is being deleted

        Returns:
            List: The list of values after the deletion

        """
        # ! To do this, we need first to check whether the value to delete is the first one
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
        else:
            # ! Traverse to the node before the node to delete
            current = self.head
            while current and current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    self.length -= 1
                current = current.next
        return self.printList()

    def deletebyIndex(self, index):
        """This method deletes a given index  of the value passed in as the parameter

        Args:
            index (int): The given index at which you are deleting the node

        Returns:
            List: The list of values after the deletion
        """
        if index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            prev_to_index_node = self.traverseTo(index-1)
            if index == self.length - 1:
                self.tail = prev_to_index_node
            to_delete = prev_to_index_node.next
            prev_to_index_node.next = to_delete.next
            self.length -= 1
        return self.printList()

    def insert(self, value, index):
        """Insert a value at a given index

        Args:
            value (Any): The value that would hold the new node
            index (int): The given index at which you are inserting the new node
        Returns:
            List: The list of values after the insertion
        """
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            prev_node = self.traverseTo(index-1)
            pointer_to_next_node = prev_node.next
            prev_node.next = NodeList(value, pointer_to_next_node)
        self.length += 1
        return self.printList()

    def reverse(self):
        """This functions creates the reversed linked list

        Returns:
            List: The list of values after the reversal
        """
        current = self.head
        prev = None
        while current:
            next_value = current.next
            current.next = prev
            prev = current
            current = next_value
        self.head = prev
        return self.printList()

    def traverseTo(self, index):
        """Traverse to a given index of the linked list

        Args:
            index (int): The value of the index you are traversing to

        Returns:
            NodeList: The node at index = {index}
        """
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


if __name__ == "__main__":
    # TestCase
    myLinkedList = SinglyLinkedList(1)
    myLinkedList.append(2)
    myLinkedList.append(3)
    myLinkedList.append(4)
    myLinkedList.prepend(12)
    myLinkedList.insert(5, 2)
    print(myLinkedList.deletebyIndex(2))
    print(myLinkedList.reverse())
