

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBST(array):
    if len(array) == 0:
        return None
    middle = len(array)//2
    root = TreeNode(array[middle])
    root.left = createBST(array[:middle])
    root.right = createBST(array[middle+1:])

    return root


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = createBST(array)
