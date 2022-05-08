class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverseInOrder(node, output):
    if (node.right):
        traverseInOrder(node.right, output)
    output.append(node.value)
    if (node.left):
        traverseInOrder(node.left, output)
    return output


def findKthLargestValueInBst(tree, k):
    # Write your code here
    values = traverseInOrder(tree, [])
    return values[k-1]


if __name__ == "__main__":
    root = TreeNode(15)
    root.left = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right = TreeNode(20)
    root.right.left = TreeNode(17)
    root.right.right = TreeNode(22)
    print(findKthLargestValueInBst(root, 3))
