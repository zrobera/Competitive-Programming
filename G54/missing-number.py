class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for i,num in enumerate(nums):
            sum1 += num
            sum2 += i
        sum2 += len(nums)
        return sum2 -sum1