class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        min_radius = float('-inf')

        def closest_heater(heater, house):
            low, high = 0, len(heater) - 1
            result = 0

            while low <= high:
                mid = (low + high) // 2

                if abs(heater[mid] - house) < abs(heater[result] - house):
                    result = mid

                if heater[mid] == house:
                    return mid
                elif heater[mid] < house:
                    low = mid + 1
                else:
                    high = mid - 1

            return result

        for house in houses:
            closest_h = closest_heater(heaters, house)
            min_radius = max(min_radius, abs(heaters[closest_h] - house))

        return min_radius