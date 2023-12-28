class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        maxm = 0

        for i in range(1,len(points)):
            x1,y1 = points[i-1]
            x2,y2 = points[i]
            maxm = max(maxm, x2-x1)
        
        return maxm

        