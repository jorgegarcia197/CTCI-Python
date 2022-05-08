class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def DFSinOrder(root, output):
    return traverseInOrder(root, output)


def traverseInOrder(node, output):
    if (node.left):
        traverseInOrder(node.left, output)
    output.append(node.val)
    if (node.right):
        traverseInOrder(node.right, output)
    return output


def successor_naive(root, node):  # O(n) space and time
    output = DFSinOrder(root, [])
    if node in output:
        return output[output.index(node)+1]
    else:
        return None


def leftmost(root):
    currentNode = root
    while currentNode.left:
        currentNode = currentNode.left
    return currentNode


def rightMostParent(node):
    currentNode = node
    while currentNode.parent and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent


def successor_optimal(root, node):
    # Two things happen here, firstly we find the leftmost node of the right subtree and then we find the rightmost parent of the left subtree
    if node.right:
        successor = leftmost(node.right)
    else:
        successor = rightMostParent(node)
    return successor


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.parent = root
    root.right = TreeNode(3)
    root.right.parent = root
    root.left.left = TreeNode(4)
    root.left.left.parent = root.left
    root.left.right = TreeNode(5)
    root.left.right.parent = root.left
    root.left.left.left = TreeNode(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    print(successor_optimal(root, node).val)
