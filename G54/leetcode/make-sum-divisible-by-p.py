class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dictt = {0:-1}
        prefix_sum = 0
        total = sum(nums)
        target = total%p
        if target == 0:
            return 0
        minm = float('inf')
        for j in range(len(nums)):
            num = nums[j]
            prefix_sum += num
            rem = prefix_sum % p
            if (rem - target)%p in dictt:
                minm = min(minm, j -dictt[(rem - target)%p])
            dictt[rem] = j
        return minm if minm != float('inf') and minm != len(nums) else -1
        