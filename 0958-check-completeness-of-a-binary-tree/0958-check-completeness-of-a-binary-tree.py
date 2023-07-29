# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        isLast = False
        while queue:
            cur = queue.popleft()
            if not cur:
                isLast = True
            else:
                if isLast:
                    return False
                queue.append(cur.left)
                queue.append(cur.right)
        return True
        
        