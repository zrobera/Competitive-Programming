class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []        
        def backtrack(nums, arr):
            if not nums:
                ans.append(arr.copy())
                return
            for i in range(len(nums)):
                arr.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], arr)
                arr.pop()
            return ans
        
        return backtrack(nums, [])