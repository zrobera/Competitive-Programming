mport math
class Solution:
    def kClosest(self,points, k):
        distances = [(math.sqrt(point[0]**2 + point[1]**2), point) for point in points]
        distances.sort()
        return [point for (distance, point) in distances[:k]]
