class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0

        curr = points[0]

        for i in range(1,len(points)):
            start = points[i][0]
            end = points[i][1]
            if start > curr[1]:
                arrows += 1
                curr = points[i]
            curr[0] = start
            curr[1] = min(curr[1], end)
        arrows += 1
        return arrows
        