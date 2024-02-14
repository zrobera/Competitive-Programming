class Solution:
    def minimumSteps(self, s: str) -> int:
        last_one = len(s)
        swaps = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                swaps += last_one-i-1
                last_one -= 1
        return swaps