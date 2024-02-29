class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(candidates,combinations):
            if sum(combinations) == target:
                ans.append(combinations.copy())

            if not candidates or sum(combinations) > target:
                return
            
            for i in range(len(candidates)):
                combinations.append(candidates[i])
                backtrack(candidates[i:],combinations)
                combinations.pop()
        backtrack(candidates, [])
        return ans