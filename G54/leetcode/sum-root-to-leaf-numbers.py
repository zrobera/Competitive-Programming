# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return []

            left = helper(root.left)
            right = helper(root.right)

            if not left and not right:
                return [str(root.val)]

            for i in range(len(left)):
                left[i] = str(root.val) + left[i]
            for i in range(len(right)):
                right[i] = str(root.val) + right[i]

            return [*left,*right]
        
        paths = helper(root)
        total = 0
        for path in paths:
            total += int(path)
        return total
