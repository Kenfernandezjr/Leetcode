# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorderTraversal(root, nums):
            if root:
                inorderTraversal(root.left, nums)
                nums.append(root.val)
                inorderTraversal(root.right, nums)
        binarySearchList = []
        inorderTraversal(root, binarySearchList)
        results = []
        
        for i in range(1, len(binarySearchList)):
            results.append(binarySearchList[i] - binarySearchList[i - 1])
        return(min(results))