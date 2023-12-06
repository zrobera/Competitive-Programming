class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0
        total = 0
        current = 0
        for i in range(n):
            week  = i//7 + 1
            i = i%7 
            total += week + i
        return total


        