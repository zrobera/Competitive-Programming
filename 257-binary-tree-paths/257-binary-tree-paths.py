# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack, ans = [],[]
        if root:
            stack.append((root, ""))
        while stack:
            cur, path = stack.pop()
            if not cur.left and not cur.right:
                ans.append(path + str(cur.val))
            if cur.right:
                stack.append((cur.right, path+str(cur.val)+ "->"))
            if cur.left:
                stack.append((cur.left, path + str(cur.val) + "->"))
        return ans