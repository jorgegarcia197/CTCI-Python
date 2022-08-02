from collections import deque
from tkinter.tix import Tree
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = self.traverseInOrder(root, [])

    def next(self) -> int:
        return self.queue.pop()

    def hasNext(self) -> bool:
        return len(self.queue) >= 1

    def traverseInOrder(self, node, output):
        if node.right:
            self.traverseInOrder(node.right, output)
        output.append(node.val)
        if node.left:
            self.traverseInOrder(node.left, output)
        return output


if __name__ == "__main__":
    root = TreeNode(7, left=TreeNode(3), right=TreeNode(
        15, left=TreeNode(9), right=TreeNode(20)))
    params = ["next", "next", "hasNext", "next",
              "hasNext", "next", "hasNext", "next", "hasNext"]
    obj = BSTIterator(root)
    for param in params:
        if param == "next":
            print(obj.next())
        elif param == "hasNext":
            print(obj.hasNext())
