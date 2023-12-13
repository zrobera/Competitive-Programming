class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        maxm = 0

        for i,num in enumerate(nums):
            count = 1
            current  = num
            if num-1 not in sets:
                while True:
                    if current + 1 in sets:
                        count += 1
                        current += 1
                    else:
                        break
            maxm = max(maxm, count)
        return maxm

                


        
        