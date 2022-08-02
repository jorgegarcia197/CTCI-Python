#* https://leetcode.com/problems/path-sum/
#! Easy Question

""" Description: 
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.count_target(root, 0)

        
    def count_target(self,node, current_sum, targetSum):
        if not node:
            return 
        current_sum += node.val
        if not node.left and not node.right:
            if current_sum == targetSum:
                return True
        if node.left:
            if self.count_target(node.left, current_sum):
                return True
        if node.right:
            if self.count_target(node.right, current_sum):
                return True
        return False
    

        