""" This represents a node of a singly linked list"""


class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value
