class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            right = i+1
            while right < len(nums):
                if nums[i] + nums[right] < target:
                    ans += 1
                else:
                    break
                right += 1
            # if right == len(nums):
            #     break

        return ans
        
        