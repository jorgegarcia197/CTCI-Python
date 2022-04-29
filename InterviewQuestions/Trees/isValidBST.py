# What makes a BST valid?

# The rule that should decide whether the BST is valid or not is that all of the nodes to the left of the root should be smaller than the root, and the values to the right should be greater than the root


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateBst(tree):
    # Write your code here.
    if not tree:
        return True
    return depthFirstSearch(tree, float('-inf'), float('inf'))


def depthFirstSearch(node: TreeNode, lower: float, upper: float) -> bool:
    """This helper function would allow us to traverse the nodes and check whether the nodes below them are valid to a BST structure

    Args:
        node (TreeNode): The current node that we are evaluating on
        lower (float): The lower limit at which the BST would become invalid
        upper (float): the upper limit at which the BST would become invalid
    """
    if node.value < lower or node.value >= upper:
        # This means the value is not within the bounds of upper and lower limits
        return False
    if node.left:
        if not depthFirstSearch(node.left, lower, node.value):
            # if it has a left value, we can go and call DFS method recursively and traverse to that left node updating the upper boundary meaning it should be smaller than the current node value
            return False
    if node.right:
        if not depthFirstSearch(node.right, node.value, upper):
            # if it has a right value, we can also call DFS again to traverse to the right and update, in this case, the lower boundary, meaning it should be greater than the current node value
            return False
    # If we have traverse all of the nodes and we havent return any false statements
    return True
