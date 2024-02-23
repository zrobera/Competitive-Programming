# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1,root2,newRoot):
            if not root1:
                return root2
            if not root2:
                return root1
            newRoot.val = root1.val + root2.val
            newRoot.right = TreeNode()
            newRoot.left = TreeNode()
            newRoot.right = merge(root1.right,root2.right,newRoot.right)
            newRoot.left = merge(root1.left, root2.left, newRoot.left)
            return newRoot
        newRoot = TreeNode()
        newRoot = merge(root1,root2,newRoot)
        return newRoot
        