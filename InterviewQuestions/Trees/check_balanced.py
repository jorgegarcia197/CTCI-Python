# Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one
from typing import Optional


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:

    if not root:
        # If there is no node
        return True
    if abs(getHeight(root.left)-getHeight(root.right)) > 1:
        # This method should get the height of each subtree and whether the difference between them is more than 1, then the tree is unbalanced
        return False
    else:
        # traverse through the next subtrees
        return isBalanced(root.left) and isBalanced(root.left)


def getHeight(root):
    if not root:
        return -1
    else:
        # Get the maximum value of the heights between both of the subtrees, the +1 is just to counter the fact it can be -1 if both subtrees point to null
        return max(getHeight(root.left), getHeight(root.right))+1
