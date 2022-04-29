from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# List Of Depths
# Given a binary tree, design an algorithm which creates a linked list of all the nodest at each depth

def listOfDepths(root):
    currentNode = root
    queue = deque()
    queue.append(currentNode)
    output = []
    while len(queue) > 0:
        length_start = len(queue)
        count = 0
        temp = []
        while count < length_start:
            currentNode = queue.popleft()
            temp.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            count += 1
        output.append(temp)
    return output


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(8)
    print(listOfDepths(root))
