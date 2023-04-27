class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_stack = [] 
        min_stack = [] 
        left = 0
        length = 0
        
        for right, num in enumerate(nums):
            while max_stack and nums[max_stack[-1]] < num:
                max_stack.pop()
            while min_stack and nums[min_stack[-1]] > num:
                min_stack.pop()
            
            max_stack.append(right)
            min_stack.append(right)
            
            while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                if max_stack[0] < min_stack[0]:
                    left = max_stack.pop(0) + 1
                else:
                    left = min_stack.pop(0) + 1
            
            length = max(length, right - left + 1)
            
        return length
