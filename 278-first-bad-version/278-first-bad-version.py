# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        ans = -1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if isBadVersion(mid):
                ans = mid
                hi = mid -1
            else:
                lo = mid + 1
        return ans
