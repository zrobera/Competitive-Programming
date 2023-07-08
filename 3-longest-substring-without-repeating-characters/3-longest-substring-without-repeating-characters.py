class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = float('-inf')
        i,j = 0,0
        res= set()
        while i<len(s) and j < len(s):
            if s[i] not in res:
                res.add(s[i])
                i += 1
                max_len = max(max_len, i-j)
            else:
                res.remove(s[j])
                j += 1
        return max_len if max_len != float('-inf') else 0
                
                
            
        