class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l, r = 0, 0, 0
        n = len(s)
        map = [-1] * 256
        while r < n:
            if map[ord(s[r])] != -1:
                l = max(map[ord(s[r])] + 1, l)
            map[ord(s[r])] = r
            ans = max(ans, r - l + 1)
            r += 1
        return ans