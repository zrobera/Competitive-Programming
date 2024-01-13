class Solution:
    def balancedString(self, s: str) -> int:
        freq= Counter(s)
        changed = defaultdict(int)
        needed = 0
        n = len(s)
        for key in freq:
            if freq[key]>n/4:
                needed += 1
                changed[key] = freq[key] - n/4
                
        if len(changed) == 0:
            return 0
        left = 0
        ans = n
        curr = defaultdict(int)
        for right in range(len(s)):
            curr[s[right]] += 1
            if changed[s[right]] == curr[s[right]]:
                needed -= 1
            while needed == 0:
                ans = min(ans,right - left + 1)
                curr[s[left]] -= 1
                if curr[s[left]] < changed[s[left]]:
                    needed += 1
                left += 1
        return ans
