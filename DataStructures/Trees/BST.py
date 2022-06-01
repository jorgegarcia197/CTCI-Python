# What is a binary tree?
# all child nodes to the right must be greater than the current node
# a node can only have up to two children


# lookup O(logN)
# insert O(logN)
# delete O(logN)

from turtle import left
from TreeNode import TreeNode


def traverseInOrder(node, output):
    if (node.left):
        traverseInOrder(node.left, output)
    output.append(node.value)
    if (node.right):
        traverseInOrder(node.right, output)
    return output


def traversePreOrder(node, output):
    output.append(node.value)
    if (node.left):
        traversePreOrder(node.left, output)
    if (node.right):
        traversePreOrder(node.right, output)
    return output


def traversePostOrder(node, output):
    if (node.left):
        traversePreOrder(node.left, output)
    if (node.right):
        traversePreOrder(node.right, output)
    output.append(node.value)
    return output


def DFSPreOrder(root, output):
    return traversePreOrder(root, output)


def DFSinOrder(root, output):
    return traverseInOrder(root, output)


def DFSPostOrder(root, output):
    return traversePostOrder(root, output)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = TreeNode(value)
        if not self.root:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    # left
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    # Right
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right

    def lookup(self, value):
        if not self.root:
            return False
        currentNode = self.root
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value == currentNode.value:
                return currentNode
        return False

    def delete(self, value):
        if not self.root:
            return False
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode == value:
                # This is the interesting bit

                # Option 1
                # No right child
                if not currentNode.right:
                    if not parentNode:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right

                # Option 2
                # Right child which doesnt have a left child
                elif not currentNode.right.left:
                    if not parentNode:
                        self.root = currentNode.left
                    else:
                        currentNode.right.left = currentNode.left

                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                # Option3
                # Right child that has a left child
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if not parentNode:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
        return True


# I strongly suggest go to visualgo to check how it works and repeat this


if __name__ == "__main__":
    myTree = BinarySearchTree()
    myTree.insert(9)
    myTree.insert(4)
    myTree.insert(6)
    myTree.insert(20)
    myTree.insert(170)
    myTree.insert(15)
    myTree.insert(1)

    print(DFSPreOrder(myTree.root, []))
