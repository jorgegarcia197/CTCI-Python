from typing import Optional
# Definition for a binary tree node.

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum_count = 0
        def count_target(node, current_sum):
            if not node:
                return 
            current_sum += node.val
            if current_sum == targetSum:
                sum_count += 1
            count_target(node.left, current_sum)
            count_target(node.right, current_sum)
        def patrol(root):
            if not root:
                return
            count_target(root, 0)
            patrol(root.left)
            patrol(root.right)
        
        patrol(root)
        return sum_count


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    print(Solution().pathSum(root, 8))
