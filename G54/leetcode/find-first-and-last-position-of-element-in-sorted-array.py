class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findPosition(nums, target, True)
        end = self.findPosition(nums, target, False)
        return [start, end]


    def findPosition(self, nums, target, isFirst):
        position = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                position = mid
                if isFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return position