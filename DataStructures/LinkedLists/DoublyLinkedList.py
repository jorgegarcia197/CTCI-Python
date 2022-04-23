from DoubleNode import DoubleLinkedListNode


class DoublyLinkedList():
    """This class represents a doubly linked list"""

    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0
        if value:
            self.append(value)

    def append(self, value):
        """Append a new value to the end  Double Linked List"""
        newNode = DoubleLinkedListNode(value)
        if self.tail:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode
        if not self.head:
            self.head = newNode
        self.length += 1
        return self.head

    def prepend(self, value):
        """ Append a new value at the beggining of the LinkedList"""
        newNode = DoubleLinkedListNode(value, self.head)
        self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self.head

    def traverseTo(self, index):
        """ Traverse to a given index of the linked list"""
        current = self.head
        count = 0
        while index != count:
            count += 1
            current = current.next
        return current

    def deletebyValue(self, value):
        """This method deletes the first instance of the value passed in the parameter"""
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.length -= 1
        current = head = self.head
        while current:
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.length -= 1
            current = current.next
        self.head = head
        return self.printList()

    def insert(self, value, index):
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            node_at_index = self.traverseTo(index)
            new_node = DoubleLinkedListNode(value, next=node_at_index)
            node_at_index.prev.next = new_node
            new_node.prev = node_at_index.prev
            node_at_index.prev = new_node
            self.length += 1
        return self.printList()

    def deletebyIndex(self, index):
        """ This method deletes a given index  of the value passed in as the parameter"""
        # if index is greater than the length of the list, return
        if index >= self.length:
            return
        # If remove from head
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        # Remove from the tail
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            current = self.traverseTo(index)
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -= 1
        return self.printList()

    def printList(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    # Create a linked list and add some values
    linkedList = DoublyLinkedList(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(4)
    linkedList.prepend(15)
    print("TraverseTo: ", linkedList.traverseTo(1).value)
    print(linkedList.printList())
    print("Delete by Index: ", linkedList.deletebyIndex(3))
    print(linkedList.insert(5, 3))
