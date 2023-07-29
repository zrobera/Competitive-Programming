# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0 
        stack = [(root, float('-inf'))]
        
        while stack:
            cur, maxm = stack.pop()
            
            if cur.val >= maxm:
                count += 1
                maxm = cur.val
            if cur.left:
                stack.append((cur.left, maxm))
            if cur.right:
                stack.append((cur.right, maxm))
        
        return count
