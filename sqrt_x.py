class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x//2+1
        while low <= high:
            mid = low + (high-low)//2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                low = mid+1
            else:
                high = mid -1
        return high
        
