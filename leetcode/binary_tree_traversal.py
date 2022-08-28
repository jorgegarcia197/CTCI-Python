class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
    
    def traversePreOrder(self):
        print(self.value)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
    
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value)
    
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value)
        if self.right:
            self.right.traverseInOrder()
    
    
    def lookup(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.lookup(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.lookup(value)
        else:
            return True
    