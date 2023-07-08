class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        current_sum = 0
        min_length = float('inf')
        
        for i in range(len(nums)):
            current_sum += nums[i]

            while current_sum >= target:
                min_length = min(min_length, i - j+1)
                current_sum -= nums[j]
                j += 1
        
        return min_length if min_length != float('inf') else 0