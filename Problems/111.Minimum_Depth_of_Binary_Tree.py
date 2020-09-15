# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
            if not root:
                return 0
            
            def dfs(root, depth):
                left_depth = right_depth = float('inf')
                
                if root is None:
                    return
                
                if root.left is None and root.right is None:
                    return depth
                
                if root.left:
                    left_depth = dfs(root.left, depth + 1)
                if  root.right:
                    right_depth = dfs(root.right, depth + 1)
                
                return min(left_depth, right_depth)
            return dfs(root, 1)