class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair_sums = []
        nums.sort()
        for i in range(len(nums)//2):
            pair_sums.append(nums[i]+ nums[-(i+1)])
        return max(pair_ssums)
