class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreePath:
    def __init__(self, treediameter):
        self.treeDiameter = treediameter

    def calculate_path(self, node: BinaryTree):
        if not node:
            return 0

        leftHeight = self.calculate_path(node.left)
        rightHeight = self.calculate_path(node.right)

        currentDiameter = leftHeight + rightHeight
        self.treeDiameter = max(currentDiameter,  self.treeDiameter)

        return max(leftHeight, rightHeight) + 1


def binaryTreeDiameter(tree):
    # Write your code here.
    max_diameter = 0
    treePath = TreePath(max_diameter)
    treePath.calculate_path(tree)
    return treePath.treeDiameter


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.left.left = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.right = BinaryTree(2)

    print(binaryTreeDiameter(root))
