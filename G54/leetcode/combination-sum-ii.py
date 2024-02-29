class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(nums, combinations):
            if sum(combinations) == target:
                ans.append(combinations.copy())
            if not nums or sum(combinations) > target:
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                combinations.append(nums[i])
                backtrack(nums[i+1:], combinations)
                combinations.pop()
        candidates.sort()
        backtrack(candidates,[])
        return ans
       