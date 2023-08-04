class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
    
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(heap, -diff)
                bricks -= diff
                
                if bricks < 0:
                    if ladders > 0:
                        bricks += -heapq.heappop(heap)
                        ladders -= 1
                    else:
                        return i
        return len(heights) - 1
        