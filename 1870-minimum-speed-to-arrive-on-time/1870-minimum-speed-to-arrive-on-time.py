class Solution:
    def isValidSpeed(self, dists: List[int], speed: int, hour: float) -> bool:
        hours_taken = 0
        for dist in dists[:-1]:
            hours_taken += math.ceil(dist / speed)
        hours_taken += dists[-1] / speed  # Last distance does not require ceiling
        return hours_taken <= hour
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:    
        low, high = 1, int(1e7)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.isValidSpeed(dist, mid, hour):
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans if ans else -1
