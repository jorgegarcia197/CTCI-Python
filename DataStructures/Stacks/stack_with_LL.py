
class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """ Returns the top element of the stack """
        return self.top.value

    def push(self, value):
        """ Pushes a value onto the stack """
        if self.isEmpty():
            self.top = NodeList(value)
            self.bottom = self.top
        else:
            self.top = NodeList(value, self.top)

        self.length += 1

    def pop(self):
        """ Pops the top element of the stack """
        # basically is pop from head of the LL
        if self.isEmpty():
            return None
        to_delete = self.top
        self.top = self.top.next
        self.length -= 1
        return to_delete.value

    def isEmpty(self):
        """ Returns True if the stack is empty """
        return self.length == 0


if __name__ == "__main__":
    stack = Stack()
    for value in ["Google", "Udacity", "Amazon"]:
        stack.push(value)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
