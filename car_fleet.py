class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        fleets = []
        for pos,spd in cars:
            time_to_dist = (target - pos) / spd
            if not fleets or time_to_dist > fleets[-1][1]:
                fleets.append((pos, time_to_dist))
            else:
                continue
        
        return len(fleets)            
