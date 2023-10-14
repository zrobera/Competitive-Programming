class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        answer = 0
        piles.sort()
        for i in range(1, len(piles)//3+1):
            answer += piles[-2*i]
        return answer