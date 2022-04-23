

class Queue():
    def __init__(self):
        self.items = []

    def popleft(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)

    def append(self, item):
        self.items.insert(0, item)

    def peek(self):
        return self.items[0] if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.items) == 0

    @property
    def length(self):
        return len(self.items)


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.append(1)
    myQueue.append(2)
    myQueue.append(3)
    print(myQueue.peek())
    print("Length before popping:", myQueue.length)
    print(myQueue.popleft())
    print("Length after popping:", myQueue.length)
    print(myQueue.peek())
