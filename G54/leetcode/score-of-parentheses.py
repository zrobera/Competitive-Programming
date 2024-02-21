class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        d = 0
        for i,char in enumerate(s):
            if char == "(":
                d += 1
            else:
                d -= 1
                if s[i-1] == "(":
                    ans += 2**d
        return ans

        