class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(reverse = True)
        
        is_all_zero = True
        for i in range(len(nums)):
            swap = False
            if nums[i] != "0":
                is_all_zero = False
            for j in range(len(nums)-i-1):
                if nums[j]+nums[j+1] < nums[j+1]+nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if not swap:
                break

        return "".join(nums) if not is_all_zero else "0"       