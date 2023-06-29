class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = float('-inf')
        d = 0
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]
            
            if i >= k - 1:
                d = s / k
                m = max(m, d)
                s -= nums[i - (k - 1)]
        
        return m
        