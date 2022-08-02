from typing import Optional

# ! Given a binary tree, determine if it is height-balanced.

#! For this problem, a height-balanced binary tree is defined as:

#! A binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Determine whether the tree is balanced or not. \n
        A binary tree in which the left and right subtrees of every node differ in height by no more than 1."""
        # * If it does not hove a root node -> then you can´t go thru the algo and it is True
        if not root:
            return True
        # * if the absolute value of both of the heights of the subtrees is greater than 1 then it mean is not balanced -> False
        if abs(self.get_height(root.left)-self.get_height(root.right)) > 1:
            return False
        # * Recursively call isBalanced function for both of the subtrees
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, root):
        """ Get the height of both of the subtrees recursively by doing a DFS algorithm"""
        if not root:
            return -1
        # * Return the maximum height of both of the subtrees and adding one to counter the fact that is equal to -1, to make it 0
        # ! # Get the maximum value of the heights between both of the subtrees, the +1 is just to counter the fact it can be -1 if both subtrees point to null
        return max(self.get_height(root.left), self.get_height(root.right))+1
