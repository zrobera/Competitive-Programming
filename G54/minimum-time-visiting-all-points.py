class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            point = points[i]
            x = abs(point[0] - points[i+1][0])
            y = abs(point[1] - points[i+1][1])
            time += max(x,y)
        return time      
        