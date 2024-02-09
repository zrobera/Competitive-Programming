class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [int(s[0])]

        for i in range(1, len(s)):
            prefix_sum.append(prefix_sum[i-1] + int(s[i]))
       
        maxm = 0
        for j in range(1,len(s)):
            ones = prefix_sum[-1] - prefix_sum[j-1]
            zeros = j - prefix_sum[j-1]
            score = ones + zeros
            maxm = max(score, maxm)
        return maxm
        