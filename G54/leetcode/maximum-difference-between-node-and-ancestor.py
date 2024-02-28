# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_difference = 0
        def helper(root,minm,maxm):
            if not root:
                return

            self.max_difference = max(self.max_difference,abs(root.val - maxm),abs(root.val - minm))
            maxm = max(root.val,maxm)
            minm = min(root.val, minm)
            helper(root.left, minm,maxm)
            helper(root.right,minm,maxm)
        helper(root,root.val,root.val)
        return self.max_difference
            