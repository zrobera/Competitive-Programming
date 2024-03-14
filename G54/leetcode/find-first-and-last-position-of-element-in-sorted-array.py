class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        first = bisect_left(nums,target)
        last = bisect_right(nums,target)-1
        # print(first,last)
        return [first,last] if first < len(nums) and nums[first] == target else [-1,-1]