class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0]*1001

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        if changes[0] > capacity:
            return False
        for i in range(1,len(changes)):
            changes[i] += changes[i-1]
            if changes[i] > capacity:
                return False
        return True
        