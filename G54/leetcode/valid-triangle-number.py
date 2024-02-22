class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        ans = 0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            left,right = i+1, len(nums)-1
            while left < right:
                if nums[i] < nums[left]+nums[right]:
                    ans += right - left
                    left += 1
                else:
                    right -= 1
        return ans


                
