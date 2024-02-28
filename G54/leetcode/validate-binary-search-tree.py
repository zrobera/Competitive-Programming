# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,minm, maxm):
            if not root:
                return True

            if not (minm < root.val < maxm):
                return False
            return helper(root.left,minm, root.val) and helper(root.right,root.val, maxm)
        return helper(root,float('-inf'), float('inf'))
        