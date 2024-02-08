class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dictt = {0:1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += dictt.get((prefix_sum -goal),0)
            dictt[prefix_sum] = dictt.get(prefix_sum,0) + 1
        return ans