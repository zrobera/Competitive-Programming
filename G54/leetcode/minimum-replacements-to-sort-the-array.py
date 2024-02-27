class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        operations = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > prev:
                spaces = math.ceil(nums[i]/prev)
                prev = nums[i] // spaces
                operations += spaces-1
            else:
                prev = nums[i]

        return operations