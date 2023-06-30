class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count= 0
        for i in logs:
            if i=="./":
                continue
            elif count and i=="../":
                count -= 1
            elif i!='../':
                count += 1
        return count
        