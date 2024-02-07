class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        if prefix_sum[len(nums)-1] - nums[0] == 0:
            return 0
        for i in range(1,len(nums)):
            if prefix_sum[i-1] == (prefix_sum[len(nums)-1] - prefix_sum[i]):
                return i
        return -1
