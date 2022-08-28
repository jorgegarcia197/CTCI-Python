class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        output = 0 
        
        value = traverseInOrder(root,output,high,low)
        
        return value
    
def traverseInOrder(node,output,high,low):
            if not node:
                return 0 
            if node.val >= low and node.val <= high:
                output += node.val
            if node.val < low:
                traverseInOrder(node.right,output,high,low)
            else:
                traverseInOrder(node.left,output,high,low)
                traverseInOrder(node.right,output,high,low)
            return output 
        
