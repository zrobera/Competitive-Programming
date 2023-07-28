# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        flag = True
        while queue:
            if flag:
                ans.append([node.val for node in queue])
            else:
                ans.append([queue[i].val for i in range(len(queue)-1,-1,-1)])
            for i in range(len(queue)):   
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            flag = not flag

        return ans
        