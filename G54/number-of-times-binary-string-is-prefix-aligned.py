class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxm = 0
        count = 0
        for i in range(len(flips)):
            maxm = max(maxm,flips[i])
            if i+1 == maxm:
                count += 1
        return count

            
        