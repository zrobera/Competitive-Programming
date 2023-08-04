class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.streams = nums
        heapq.heapify(self.streams)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.streams, val)
        while len(self.streams) > self.k:
            heapq.heappop(self.streams)
        return self.streams[0]