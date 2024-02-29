class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums, combinations):
            ans.append(combinations.copy())

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                combinations.append(nums[i])
                backtrack(nums[i+1:], combinations)
                combinations.pop()
        nums.sort()
        backtrack(nums,[])
        return ans