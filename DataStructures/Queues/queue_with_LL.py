class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


class Queue():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def popleft(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1

    def append(self, item):
        newNode = NodeList(item)
        if self.isEmpty():
            self.top = newNode
            self.bottom = newNode
        else:
            self.bottom.next = newNode
            self.bottom = newNode
        self.length += 1

    def peek(self):
        return self.top.value

    def isEmpty(self):
        return self.length == 0
