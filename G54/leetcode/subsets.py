class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums, combinations):
            ans.append(combinations.copy())

            for i in range(len(nums)):
                combinations.append(nums[i])
                backtrack(nums[i+1:], combinations)
                combinations.pop()
        backtrack(nums,[])
        return ans
        