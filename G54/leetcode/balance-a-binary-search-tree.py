# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,arr):
            if not root:
                return
            dfs(root.left,arr)
            arr.append(root.val)
            dfs(root.right,arr)
        
        arr = []
        dfs(root,arr)
        return arr
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,start,end):
            if start >= end:
                return None
            mid = (start + end)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums,start,mid)
            root.right = helper(nums,mid+1,end)
            return root
        return helper(nums,0,len(nums))
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArr = self.inorderTraversal(root)
        return self.sortedArrayToBST(sortedArr)
        