""" This represents a double linked list node"""


class DoubleNode():
    """ This represents a single node of a double linked list """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
