
#! https://leetcode.com/problems/my-calendar-i/

""" You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 """

# ! I really like this explanation of the problem, basically it is implementing a BST that has two different attributes, the end and the start. and it is based on the hint 1
# ! With the Node class, we basically implement a BST with the start and end attributes, and the insert method is the direct implementation of an insertion within a BST,

# * whenever the start is greater or equal to the end, and there is not right node, we insert the node as the right node, if there is, we recursevily call the insert method on the right node
# * Otherwise, if the end is less or equal to the start of that node, we insert the node as the left node, if there is, we recursevily call the insert method on the left node
# * else, we return False -> This allow us to prevent double bookings


# * Hint 1: Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


# ! For the book method, we basically check if there is not root node in the tree, if there is, we insert the node, if not, we call the insert metod of the root node and return whether it was a succesful insertion or not (True or False)


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
