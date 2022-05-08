
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateBST(tree):
    # Write your code here.
    if not tree:
        return True
    if tree.left:
        if tree.left.value < tree.value:
            validateBST(tree.left)
        else:
            return False
    if tree.right:
        if tree.right.value > tree.value:
            validateBST(tree.right)
        else:
            return False


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(13)
    root.right.left.right = TreeNode(14)
    root.right.right = TreeNode(22)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)

    print(validateBST(root))
