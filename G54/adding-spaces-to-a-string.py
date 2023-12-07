class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        num = 0
        for idx in spaces:
            idx += num
            s = s[:idx]+ " " + s[idx:]
            num += 1
        return s
        