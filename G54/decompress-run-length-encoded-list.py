class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            ans.extend([nums[i+1]]*nums[i])
            i += 2
        return ans
        