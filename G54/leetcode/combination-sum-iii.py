class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(nums, combinations):
            if len(combinations) == k and sum(combinations) == n:
                ans.append(combinations.copy())
            if not nums or sum(combinations) > n:
                return
            for i in range(len(nums)):
                combinations.append(nums[i])
                backtrack(nums[i+1:], combinations)
                combinations.pop()
        nums = [num+1 for num in range(9)]
        backtrack(nums, [])
        return ans

        