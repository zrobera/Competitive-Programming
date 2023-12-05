class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        remaining = capacity
        for i,plant in enumerate(plants):
            if remaining >= plant:
                steps += 1
                remaining -= plant
            if i+1 < len(plants) and remaining < plants[i+1]:
                steps += 2*(i+1)
                remaining =  capacity
        return steps

            
