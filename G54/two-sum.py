class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        for i in range(len(nums)):
            dicts[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in dicts and dicts[target - nums[i]] != i:
                return [i, dicts[target - nums[i]]]

        return []