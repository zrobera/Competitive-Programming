# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums):
            if not nums:
                return
            maxm = -1
            idx = 0
            for i in range(len(nums)):
                if nums[i] > maxm:
                    maxm = nums[i]
                    idx = i
            
            root = TreeNode(maxm)
            root.left = buildTree(nums[0:idx])
            root.right = buildTree(nums[idx+1:])
            return root
        return buildTree(nums)
        