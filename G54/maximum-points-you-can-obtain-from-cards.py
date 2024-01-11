class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        maxm = -1

        total = sum(cardPoints)
        curr = 0
        for right in range(len(cardPoints)):
            curr += cardPoints[right]
            if right-left+1 == len(cardPoints)-k:
                maxm = max(maxm, total-curr)
                curr -= cardPoints[left]
                left += 1

        return maxm if maxm != -1 else total

        