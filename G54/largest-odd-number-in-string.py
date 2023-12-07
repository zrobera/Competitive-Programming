class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i,char in enumerate(num):
            if int(char)%2 != 0:
                ans = num[:i+1]
        return ans

        