import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lists = []
        for i in range(rowIndex+1):
            combinations = math.comb(rowIndex, i)
            lists.append(combinations)
        return lists