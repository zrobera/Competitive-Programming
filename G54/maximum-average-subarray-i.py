class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxm = float('-inf')

        left = 0
        curr = 0
        for right in range(len(nums)):
            if right-left == k-1:
                curr += nums[right]
                maxm = max(curr,maxm)
                curr -= nums[left]
                left += 1
            else:
                curr += nums[right]
        
        return maxm/k


        