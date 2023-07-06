class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for num in nums:
            sum1 += num
        for i in range(len(nums)+1):
            sum2 += i
        return sum2 -sum1