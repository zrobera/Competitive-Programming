# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = []
        summ = 0
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                if not cur.left.left and not cur.left.right:
                    summ += cur.left.val
            if cur.right:
                stack.append(cur.right)
        return summ

