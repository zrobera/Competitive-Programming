class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums, comb):
            ans.append(comb)
            for i in range(len(nums)):
                backtrack(nums[i+1:],comb+[nums[i]])
        backtrack(nums, [])
        return ans

        