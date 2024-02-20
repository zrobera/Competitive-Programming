class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        temp = []
        arr = self.getRow(rowIndex-1)
        for i in range(1,len(arr)):
            temp.append(arr[i]+arr[i-1])
        return [1] + temp + [1]
        