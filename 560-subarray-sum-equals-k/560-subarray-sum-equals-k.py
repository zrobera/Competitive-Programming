class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = {0:1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += dictt.get((prefix_sum -k),0)
            dictt[prefix_sum] = dictt.get(prefix_sum,0) + 1
        return ans


        