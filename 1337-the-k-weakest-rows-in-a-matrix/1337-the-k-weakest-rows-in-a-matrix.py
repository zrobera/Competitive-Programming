class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            count = mat[i].count(1)
            heapq.heappush(heap, (count,i))
        ans = [heapq.heappop(heap)[1] for _ in range(k)]
        return ans


