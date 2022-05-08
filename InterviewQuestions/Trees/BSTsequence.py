class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bstSequence(root):
    return [PreorderR(root, []), Preorder(root, [])]


def PreorderR(node, output):
    output.append(node.value)
    if node.right:
        PreorderR(node.right, output)
    if node.left:
        PreorderR(node.left, output)
    return output


def Preorder(node, output):
    output.append(node.value)
    if node.left:
        Preorder(node.left, output)
    if node.right:
        Preorder(node.right, output)

    return output


if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right = TreeNode(25)
    print(bstSequence(root))
