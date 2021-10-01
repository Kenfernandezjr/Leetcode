# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderDfs(root, nums):
            if root:
                nums.append(root.val)
                preorderDfs(root.left, nums)
                preorderDfs(root.right, nums)
        a = []
        preorderDfs(root, a)
        return a