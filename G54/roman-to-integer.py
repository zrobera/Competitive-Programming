class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {"I": 1, "V": 5, "X":10, "L":50,"C": 100, "D": 500, "M":1000}
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if i+1 < len(s) and dicts[s[i]] < dicts[s[i+1]]:
                ans -= dicts[s[i]]
            else:
                ans += dicts[s[i]]
            print(ans)
        return ans
            

        
        