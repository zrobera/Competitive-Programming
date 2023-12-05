class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        total = 0
        
        for i in range(len(distance)):
            total += distance[i]
            if (i >= start and i< destination) or (i >= destination and i< start):
                clockwise += distance[i]
        anti_clockwise = total - clockwise
        return min(clockwise, anti_clockwise)
        
        