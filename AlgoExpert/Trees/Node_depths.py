from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# For this problem, it is better to use the BFS because you are traversing the tree in a level order fashion.

# This is a variation of the normal BFS because you have to keep count of at which level youre at
# The only way to do this is with the len of the queue at each level


def BFS(root):
    queue = deque()
    queue.append(root)
    suma = 0
    level = 0
    while queue:
        length_at_start = len(queue)
        count = 0
        while count < length_at_start:
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            count += 1
            suma += level
        level += 1
    return suma


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(BFS(root))
