# Design an algorithm and write code to find the first common ancestor of two TreeNodes in a binary tree. Avoid storing additional TreeNodes in a data structure. NOTE: This is not necessarily a binary search tree.

# The first common ancestor is the lowest common ancestor of the two TreeNodes.

# 10 : if each TreeNode has a link to its parent, we could leverage the approach from the last question. However , our interviewer might not let us make this assumption

# 16: The first common ancestor is the deepest TreeNode such that p and q are both descendants. Think abount how you might identify this TreeNode.

# 28: How would you figure out if p is a descendent of a TreeNode n?

# 36 : Start with the root. Can you identify if root is the first common ancestor? if it is not, can you identify which side of root the first common ancestor is on?

# 46 : Try a recursive approach.

# 70 return the first common ancestor of two TreeNodes in a binary tree. p if p is in the tree but not q, q if q is in the tree but not p, or null if neither p nor q are in the tree.

from multiprocessing.dummy import current_process


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def firstCommonAncestor(root, p, q):
    currentNode = root

    if not currentNode:
        return currentNode
    if any([currentNode.val == p, currentNode.val == q]):
        return currentNode

    left_ca = firstCommonAncestor(currentNode.left, p, q)
    right_ca = firstCommonAncestor(currentNode.right, p, q)

    if left_ca and right_ca:
        return currentNode

    return left_ca if left_ca else right_ca


class Solution:

    def firstCommonAncestor(self, root, p, q):
        currentNode = root

        if not currentNode:
            return currentNode
        if any([currentNode.val == p, currentNode.val == q]):
            return currentNode

        left_ca = self.firstCommonAncestor(currentNode.left, p, q)
        right_ca = self.firstCommonAncestor(currentNode.right, p, q)

        if left_ca and right_ca:
            return currentNode

        return left_ca if left_ca else right_ca

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentNode = root

        # Base case
        if not currentNode:
            return currentNode

        # if we have any match within the p or q values return that node so we can keep track of it
        if any([currentNode.val == p, currentNode.val == q]):
            return currentNode

        # now, we can traverse, first to the left and then to the right

        left = self.lowestCommonAncestor(currentNode.left, p, q)
        right = self.lowestCommonAncestor(currentNode.right, p, q)

        if left and right:
            return currentNode

        return left if left else right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    solution = Solution()
    print(solution.lowestCommonAncestor(root, 5, 1).val)

    print(solution.firstCommonAncestor(root, 5, 4).val)
