class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = float('inf')
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                minm = min(minm, right-left+1)
                curr -= nums[left]
                left += 1
        return minm if minm != float('inf') else 0

        