class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        current_sum = 0
        min_length = float('inf')
        
        while right < len(nums):
            current_sum += nums[right]
            right += 1
            
            while current_sum >= target:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0