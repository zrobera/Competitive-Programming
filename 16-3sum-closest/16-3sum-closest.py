class Solution:
    def threeSumClosest(self, nums, target):
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        if len(nums) < 3:
            return 0
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    j += 1
                    k -= 1
                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return closest

        