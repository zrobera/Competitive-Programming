class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        freq = Counter(nums)

        i = 0
        operations = 0
        for key in freq:
            operations += freq[key]*i
            i += 1
        return operations


        