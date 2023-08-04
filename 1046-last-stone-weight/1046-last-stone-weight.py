class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        for i in range(len(stones) - 1, 0, -1):
            stones[i - 1] = stones[i] - stones[i - 1]
            stones.sort()
        return stones[0]