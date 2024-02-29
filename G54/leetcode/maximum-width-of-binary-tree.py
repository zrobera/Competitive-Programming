# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 1
        while queue:
            minm,maxm = float('inf'),float('-inf')
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    cur.left.val = 2*cur.val
                    maxm = max(cur.left.val,maxm)
                    minm = min(cur.left.val,minm)
                    queue.append(cur.left)
                if cur.right:
                    cur.right.val = 2*cur.val+1
                    maxm = max(cur.right.val,maxm)
                    minm = min(cur.right.val,minm)
                    queue.append(cur.right)
            if minm != float('inf'):
                ans = max(ans, maxm-minm+1)

        return ans