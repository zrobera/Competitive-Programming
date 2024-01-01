class Solution:
    def kClosest(self,points, k):
        distances = []
        for point in points:
            distances.append((math.sqrt(point[0]**2 + point[1]**2), point))
        distances.sort()
        return [point for (distance, point) in distances[:k]]
