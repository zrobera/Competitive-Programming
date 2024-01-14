class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)

        curr = defaultdict(int)
        extras = defaultdict(int)
        ans = [float('-inf'), float('inf')]
        minm = float('inf')
        left = 0

        for right in range(len(s)):
            if s[right] in target:
                if target[s[right]] > curr[s[right]]:
                    curr[s[right]] += 1
                else:
                    extras[s[right]] += 1
            while curr == target:
                if right-left+1 < minm:
                    minm = right-left+1
                    ans = [left,right+1]
                if s[left] in curr:
                    if extras[s[left]] > 0:
                        extras[s[left]] -= 1
                    else:
                        curr[s[left]] -= 1
                left += 1
            
        return s[ans[0]:ans[1]] if minm != float('inf') else ""

        