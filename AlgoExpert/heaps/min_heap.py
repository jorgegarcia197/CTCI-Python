# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        parentNodes = (len(array)-2) // 2
        for currentIdx in reversed(range(parentNodes+1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array
    def is_empty(self):
        return len(self.heap) == 0

    def siftDown(self, idx, endIdx, heap):
        childOne = idx * 2 + 1
        while childOne <= endIdx:
            childTwo = idx * 2 + 2 if idx * 2 + 2 <= endIdx else -1
            if childTwo != -1 and heap[childTwo] < heap[childOne]:
                to_swap = childTwo
            else:
                to_swap = childOne
            if heap[to_swap] < heap[idx]:
                self.swap(idx, to_swap, heap)
                idx = to_swap
                childOne = idx * 2 + 1
            else:
                return

    def siftUp(self, idx, heap):
        parentIdx = (idx - 1) // 2
        while idx > 0 and heap[idx] < heap[parentIdx]:
            self.swap(idx, parentIdx, heap)
            idx = parentIdx
            parentIdx = (idx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        # swap first and last
        self.swap(0, len(self.heap) - 1, self.heap)
        removed_value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed_value

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
