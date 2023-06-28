class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False for _ in range(n)]
        dp[0]=True

        for i in range(n):
            if dp[i]:   # if this position is reachable
                for j in range(1,nums[i]+1):
                    if i+j<n:
                        dp[i+j]=True
                    if i+j==n-1:
                        return True
        return dp[n-1]
        