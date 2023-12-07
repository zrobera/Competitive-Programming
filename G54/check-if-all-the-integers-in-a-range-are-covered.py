class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        needed = {num for num in range(left, right+1)}
        for i,j in ranges:            
            for num in range(i,j+1):
                if num in needed:
                    needed.remove(num)
        return len(needed) == 0
            

        