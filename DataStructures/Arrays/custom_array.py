
class myOwnArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def append(self, value):
        self.data[self.length] = value
        self.length += 1
        return None

    def pop(self):
        last = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last

    def delete(self, index):
        item = self.data[index]
        self.shiftitems(index)
        return item

    def shiftitems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return None


new_array = myOwnArray()
new_array.append(1)
new_array.append("hello mofo")
print("get(0): ", new_array.get(0))
print("pop: ", new_array.pop())
