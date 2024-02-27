# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicts = defaultdict(int)
        def helper(root):
            if not root:
                return
            dicts[root.val] += 1
            helper(root.left)
            helper(root.right)
        helper(root)
        maxm = max(dicts.values())
        ans = []
        for key,value in dicts.items():
            if value == maxm:
                ans.append(key)
        return ans
            
            

        