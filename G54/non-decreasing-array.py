class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ans= 0
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                ans += 1
                if ans > 1:
                    return False
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
        return True