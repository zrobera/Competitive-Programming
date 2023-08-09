class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        day, i, ans = 0, 0, 0
        min_heap = []
        days = 0
        for event in events:
            days = max(days, event[1])
        
        for day in range(1, days+1):
            while i < len(events) and events[i][0] == day:
                heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heappop(min_heap)            
            if  min_heap:
                heappop(min_heap)
                ans += 1
        return ans