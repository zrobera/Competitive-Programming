class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums,comb):
            ans.append(comb)
            for i in range(len(nums)):
                if i >= 1 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[i+1:], comb + [nums[i]])
        nums.sort()
        backtrack(nums,[])
        return ans
        