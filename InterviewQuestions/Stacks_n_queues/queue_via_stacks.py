

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def _reverseList(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                print("Empty stack")
                return
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())

    # append
    def enqueue(self, value):
        self.stack1.append(value)

    # popleft
    def dequeue(self):
        self._reverseList()
        return self.stack2.pop()

    def peek(self):
        self._reverseList()
        return self.stack2[-1]
