""" Class that implements a stack using an array. """



class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.array.pop()

    def isEmpty(self):
        return len(self.array) == 0


if __name__ == "__main__":
    stack = Stack()
    for value in ["Google", "Udacity", "Amazon"]:
        stack.push(value)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
