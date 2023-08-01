class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        def backtrack(idx, comb):
            nonlocal ans
            if idx == len(cookies):
                maxm = max(comb)
                ans = min(ans,maxm)
                return
            if ans <= max(comb):
                return
            for i in range(k):
                comb[i] += cookies[idx]
                backtrack(idx+1, comb)
                comb[i] -= cookies[idx]
        ans = float('inf')
        backtrack(0,[0]*k)
        return ans

