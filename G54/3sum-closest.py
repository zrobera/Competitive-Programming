class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue 
            l = i + 1
            r = len(nums)-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                ans = min(ans, curr_sum, key= lambda x: abs(target-x))
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1  
        return ans
                