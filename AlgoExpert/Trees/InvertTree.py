def invertBinaryTree(tree):
    # Write your code here.
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def InvertBinaryTree(tree):
    return DFSPreOrder(tree, [])


def traversePreOrder(node, output):
    output.append(node.value)
    if (node.left) or node.right:
        # Switch
        temp = node.right
        node.right = node.left
        node.left = temp
    if (node.left):
        traversePreOrder(node.left, output)
    if (node.right):
        traversePreOrder(node.right, output)
    return output


def DFSPreOrder(root, output):
    return traversePreOrder(root, output)


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(DFSPreOrder(root, []))

#! INPUT
#             1
#         2       3
#     4     5    6   7
# 8     9

#! OUTPUT
#           1
#       3       2
#  7   6    5     4
#                9  8
