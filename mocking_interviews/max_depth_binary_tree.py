from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# root = 1 -> 3-> [5,6] ,2,4 ->


def maxDepth(root):
    if not root:
        return 0
    stack = deque()
    stack.append(root)
    height = 0

    while stack:
        initial_length = len(stack)-1
        counter = 0
        while counter <= initial_length:
            currentNode = stack.popleft()
            if currentNode.children:
                stack.extend(currentNode.children)
            counter += 1
        height += 1
    return height


def maxDepth_recursively(root):
    if not root:
        return 0
    height = 1
    return traverseLevel(root, height)


def traverseLevel(node, level):
    if not node.children:
        return 0
    heights = []
    for children in node.children:
        heights.append(traverseLevel(children, level+1))
    return max(heights)


if __name__ == "__main__":
    input_value = Node(
        1, children=[Node(3, children=([Node(5), Node(6)])), Node(2), Node(4)])
    print(maxDepth_recursively(input_value))
