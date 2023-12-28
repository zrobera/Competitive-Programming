class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_dict = {}

        sorted_nums = sorted(nums)

        for i, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = i

        result = [count_dict[num] for num in nums]

        return result


        