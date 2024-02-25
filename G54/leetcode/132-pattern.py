class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimums = []
        minm = float('inf')
        for num in nums:
            minm = min(minm,num)
            minimums.append(minm)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack and minimums[stack[-1]] < nums[i]:
                return True
            stack.append(i)
        return False