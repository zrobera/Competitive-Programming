class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = 0
        i = 0
        while i < len(num):
            char = num[i]
            j = i+1
            temp = char
            while j < len(num) and num[j] == char and len(temp) < 3:
                temp += num[j]
                j += 1
            if len(temp) == 3 and int(temp) >= int(ans):
                ans = temp
                i += 2
            i += 1
        return ans if ans != 0 else ""


        