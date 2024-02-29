class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1,n+1)]
        combinations = []
        
        def backtrack(i, combination):
            if len(combination) == k:
                combinations.append(combination.copy())
                return
            if i >= n:
                return
            needed = k - len(combination)
            remain = n-i
            if remain < needed:
                return
            
            combination.append(nums[i])
            backtrack(i+1, combination)
            combination.pop()
            backtrack(i+1, combination)
        
        backtrack(0, [])
        return combinations
        