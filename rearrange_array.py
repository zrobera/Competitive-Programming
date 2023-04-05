class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        res[::2], res[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]
        return res
