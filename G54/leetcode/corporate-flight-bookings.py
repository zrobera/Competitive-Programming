class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        changes = [0]*n
        for first,last,seats in bookings:
            changes[first-1] += seats
            if last < n:
                changes[last] -= seats
        for i in range(1,n):
            changes[i] += changes[i-1]
        return changes
        