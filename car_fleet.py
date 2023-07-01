class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        fleets = []
        for pos,spd in cars:
            time_to_dist = (target - pos) / spd
            if not fleets or time_to_dist > fleets[-1]:
                fleets.append(time_to_dist)     
        return len(fleets)            
