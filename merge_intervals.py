class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # If the current interval overlaps with the previous interval,
            # merge them by updating the end time of the previous interval
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            # Otherwise, add the current interval to the list of merged intervals
            else:
                merged.append(interval)
        return merged
