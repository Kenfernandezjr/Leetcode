class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        storage = 0
        if root.val >= low and root.val <= high:
            storage += root.val
        storage += self.rangeSumBST(root.left, low, high)
        storage += self.rangeSumBST(root.right, low, high)
    return storage