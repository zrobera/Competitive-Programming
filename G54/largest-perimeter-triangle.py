class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        i = 2
        ans = 0
        while i < len(nums):
            if nums[i]+nums[i-1] > nums[i-2]:
                ans = max(ans, (nums[i] + nums[i-1] + nums[i-2]))
            i += 1
        return ans

        