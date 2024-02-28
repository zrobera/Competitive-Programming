# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if not root:
                return None,0,float('inf'), float('-inf')

            left,total1,left_min,left_max = helper(root.left)
            right,total2,right_min,right_max = helper(root.right)

            if left_max < root.val < right_min:
                total = root.val + total1 + total2
                self.ans = max(self.ans, total)
                return root , total, min(root.val, left_min), max(root.val,right_max)
            return root, float('-inf'), min(root.val, left_min), max(root.val,right_max)
        helper(root)
        return self.ans
        