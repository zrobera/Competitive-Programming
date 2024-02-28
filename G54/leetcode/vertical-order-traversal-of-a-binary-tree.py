# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(col,row,root,arr):
            if not root:
                return
            arr.append([col,row,root.val])
            helper(col-1,row+1,root.left,arr)
            helper(col+1,row+1,root.right,arr)
            return arr

        arr = []
        arr = helper(0,0,root,arr)
        arr.sort()
        ans = [[]]
        curr = arr[0][0]
        i = 0
        for col,row,val in arr:
            if curr == col:
                ans[i].append(val)
            else:
                curr = col
                ans.append([val])
                i += 1
        return ans
            


