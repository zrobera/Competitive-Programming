class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        ans = 0
        odd = 0
        for value in freq.values():
            if value % 2 == 0:
                ans += value
            else:
                odd = 1
                ans += value - 1
        return ans+1 if odd else ans
