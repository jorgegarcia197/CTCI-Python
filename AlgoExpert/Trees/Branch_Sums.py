class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def DFSinOrder(root, output):
    return traverseInOrder(root, output, 0)


def traverseInOrder(node, output, suma):
    suma += node.value

    if (node.left):
        traverseInOrder(node.left, output, suma)
    if (node.right):
        traverseInOrder(node.right, output, suma)
    if (node.left is None and node.right is None):
        output.append(suma)
    return output


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(10)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(DFSinOrder(root, []))
