class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysToShip(capacity):
            numDays = 0
            curr = 0
            for weight in weights:
                if weight > capacity:
                    numDays = float('inf')
                    break
                curr += weight
                if curr > capacity:
                    curr = weight
                    numDays += 1
                if curr == capacity:
                    curr = 0
                    numDays += 1
            if curr != 0:
                numDays += 1
            return numDays
        
        lo, hi = 0, sum(weights)
        while lo < hi:
            mid = (lo+hi)//2
            if daysToShip(mid) > days:
                lo = mid + 1
            else:
                hi = mid
        return lo
