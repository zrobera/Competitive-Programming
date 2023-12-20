class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
        maxm = -1
        ans = []

        for i,num in enumerate(prefix):
            zeros = 0 if i == 0 else i-prefix[i-1]
            ones = prefix[-1] if i==0 else prefix[-1] - prefix[i-1]
            score = zeros + ones
            if score == maxm:
                ans.append(i)
            elif score > maxm:
                maxm = score
                ans = []
                ans.append(i)
        if len(nums)-prefix[-1] > maxm:
            ans = [len(nums)]
        elif len(nums)-prefix[-1] == maxm:
            ans.append(len(nums))
        return ans
        