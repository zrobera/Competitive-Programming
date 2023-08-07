class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        l = 0
        r = len(costs)-1

        while(l < candidates):
            heappush(heap, (costs[l], l))
            l += 1

        while(r >= len(costs)-candidates and r >= l):
            heappush(heap, (costs[r], r))
            r -= 1

        res = 0
        for _ in range(k):
            c, idx = heappop(heap)

            res += c

            if idx < l:
                if l <= r:
                    heappush(heap, (costs[l], l))
                    l += 1
            else:
                if l <= r:
                    heappush(heap, (costs[r], r))
                    r -= 1

        return res