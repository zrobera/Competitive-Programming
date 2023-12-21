class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        for col in range(len(strs[0])):
            for row in range(len(strs)-1):
                if ord(strs[row][col]) > ord(strs[row+1][col]):
                    ans += 1
                    break
        return ans

        