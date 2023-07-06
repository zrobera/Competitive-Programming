class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num//2+1
        while low <= high:
            mid = low + (high-low)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                low = mid+1
            else:
                high = mid -1
        return False
        