class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def DFSinOrder(root, output):
    return traverseInOrder(root, output)


def traverseInOrder(node, output):
    if (node.left):
        traverseInOrder(node.left, output)
    output.append(node.val)
    if (node.right):
        traverseInOrder(node.right, output)
    return output


def successor_naive(root, node): # O(n) space and time
    output = DFSinOrder(root, [])
    if node in output:   
        return output[output.index(node)+1]
    else:
        return None
def successor_optimal(root,node):
    ## Two things happen here, because 
    pass

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    print(DFSinOrder(root,[]))
