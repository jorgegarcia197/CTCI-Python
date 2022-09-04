from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_map = {}
        def dfs(node, x, y):
            if node:
                if x not in level_map:
                    level_map[x] = {}
                if y not in level_map[x]:
                    level_map[x][y] = []
                level_map[x][y].append(node.val)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        result = []
        for x in sorted(level_map.keys()):
            level = []
            for y in sorted(level_map[x].keys()):
                level += sorted(level_map[x][y])
            result.append(level)
        return result
    
if __name__ == "__main__":
    # A tree node from 1 to 7
    input_tree =  TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(Solution().verticalTraversal(input_tree))
    
        