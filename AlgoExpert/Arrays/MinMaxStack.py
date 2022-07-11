# Feel free to add new properties and methods to the class.
class MinMaxStack:
    values = []
    minmax = []

    def peek(self):
        # Write your code here.
        if not len(self.values):
            return None
        return self.values[-1]

    def pop(self):
        # Write your code here.
        if not len(self.values):
            return None
        self.minmax.pop()
        return self.values.pop()
    #! update the min and max if the number is either one of them

    def push(self, number):
        # Write your code here.
        new_min_max = {"min": number, "max": number}
        last_min_max = self.minmax[-1] if len(self.minmax) else None
        if last_min_max:
            new_min_max["min"] = min(number, last_min_max["min"])
            new_min_max["max"] = max(number, last_min_max["max"])
        self.minmax.append(new_min_max)
        self.values.append(number)

    def getMin(self):
        # Write your code here.
        return self.minmax[-1]["min"] if len(self.minmax) else None

    def getMax(self):
        # Write your code here.
        return self.minmax[-1]["max"] if len(self.minmax) else None


if __name__ == "__main__":
    min_max_stack = MinMaxStack()
    min_max_stack.push(2)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.push(7)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.push(1)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.push(8)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.push(3)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.push(9)
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
    min_max_stack.pop()
    print(min_max_stack.getMin())
    print(min_max_stack.getMax())
    print(min_max_stack.peek())
