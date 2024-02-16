class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        prefix = 0
        curr = 0
        x = 1
        patches = 0
        while prefix < n:
            if curr < len(nums) and nums[curr] <= x:
                prefix += nums[curr]
                curr += 1
            else:
                prefix += x
                patches += 1
            x = prefix + 1
        return patches
            
        