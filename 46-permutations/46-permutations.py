class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []        
        def backtrack(nums, arr):
            if not nums:
                ans.append(arr)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], arr + [nums[i]])
            return ans
        
        return backtrack(nums, [])
