# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorderDfs(root, nums):
            if root:
                inorderDfs(root.left, nums)
                nums.append(root.val)
                inorderDfs(root.right, nums)
        a = []
        inorderDfs(root, a)
        return a