""" This represents a double linked list node"""


class DoubleLinkedListNode():
    """ This represents a single node of a double linked list """

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
