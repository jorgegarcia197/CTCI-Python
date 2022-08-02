from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    tree_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """ Get the maximum diameter of a binary tree \n
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. \n
        The length of a path between two nodes is represented by the number of edges between them."""

        # The first thing that I have to do -> from the root node, get the maximum depth for both sides, and if it is greater than the current max height, update it

        self.calculate_path(root)
        return self.tree_diameter

    def calculate_path(self, node):
        if not node:
            return 0
        left_height = self.calculate_path(node.left)
        right_height = self.calculate_path(node.right)
        currentDiameter = left_height + right_height
        self.tree_diameter = max(self.tree_diameter, currentDiameter)

        return max(left_height, right_height) + 1
