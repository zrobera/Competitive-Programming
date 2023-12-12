class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexs = {}

        for i,num in enumerate(nums):
            indexs[num] = i

        for first,last in operations:
            old_idx = indexs[first]
            nums[old_idx] = last
            del indexs[first]
            indexs[last] = old_idx
        return nums           

            
        