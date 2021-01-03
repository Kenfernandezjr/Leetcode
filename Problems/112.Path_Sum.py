# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, run_sum):
            if not node:
                return False
            
            run_sum += node.val
            
            if node.left is None and node.right is None:
                return run_sum == sum
            
            return dfs(node.left, run_sum) or dfs(node.right, run_sum)
        return dfs(root, 0)