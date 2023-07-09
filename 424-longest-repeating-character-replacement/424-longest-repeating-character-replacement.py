class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {char:0 for char in s}
        j,ans = 0,0
        frequent = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            frequent = max(frequent,freq[s[i]])
            while i-j+1 - frequent > k:
                freq[s[j]] -= 1
                j += 1
            ans = max(ans,i-j+1)
        return ans

        