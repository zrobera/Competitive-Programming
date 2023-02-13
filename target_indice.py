class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        lists = []
        counter = 0
        for i in sortedNums:
            if i == target:
                lists.append(counter)
            counter += 1
        return lists
