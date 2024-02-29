class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                for k in range(i, j+1):
                    if s[k].lower() not in s[i:j+1] or s[k].upper() not in s[i:j+1]:
                        break
                else: 
                    ans = max(ans, s[i:j+1], key=len)   
        return ans 