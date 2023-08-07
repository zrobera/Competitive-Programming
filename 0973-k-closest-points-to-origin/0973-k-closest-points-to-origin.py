import math
class Solution:
    def kClosest(self,points, k):
        distances = [(math.sqrt(point[0]**2 + point[1]**2), point) for point in points]
        heapq.heapify(distances)
        return [heapq.heappop(distances)[1] for _ in range(k)]

