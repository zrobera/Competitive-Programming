class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 == num2 and i<j:
                    ans += 1
        return ans

        