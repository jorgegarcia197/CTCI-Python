# TODO: Follow up question
# Implement a PopAtStack
# Also, what I believe the proper solution or what I've seen is the PriorityQueue Solution


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stackOfStacks = [[]]
        self.capacity = capacity

    def push(self, val: int) -> None:
        if len(self.stackOfStacks[-1]) == self.capacity:
            self.stackOfStacks.append([])
        self.stackOfStacks[-1].append(val)

    def pop(self) -> int:
        if len(self.StackOfStacks[-1] == 0):
            if len(self.StackOfStack == 1):
                raise IndexError("pop from empty stack")
            else:
                self.StackOfStack.pop()
        self.StackOfStacks[-1].pop()
