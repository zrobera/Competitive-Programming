class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        while i<len(s):
            if i+2 < len(s) and s[i+2] == '#':
                ans += chr(int(s[i]+s[i+1])+96)
                i+= 2
            else:
                ans += chr(int(s[i])+96)
            i += 1
        return ans

        