from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverseInOrder(node, output):

    output.append(str(node.val))
    if (node.left):
        traverseInOrder(node.left, output)
    if (node.right):
        traverseInOrder(node.right, output)
    return output


def traversePreOrder(node, output):
    output.append(str(node.val))
    if (node.left):
        traversePreOrder(node.left, output)
    if (node.right):
        traversePreOrder(node.right, output)

    return " ".join(output)

def traversePreOrder_iterative(root):
    queue = deque()
    queue.append(root)
    output = []
    while queue:
        node = queue.popleft()
        output.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return " ".join(output)
        

def get_max_height(root):
    height = 0
    if not root:
        return height
    queue = deque()
    queue.append(root)
    while queue:
        height += 1
        counter = 0
        queue_len = len(queue)
        while counter < queue_len:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            counter += 1
    return height


def levelOrder(root):
    output = traversePreOrder(root, [])
    return output


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(3)
    root.right.right.left.right = TreeNode(4)
    root.right.right.right = TreeNode(6)

    print(traversePreOrder_iterative(root))
