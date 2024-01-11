class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minm = float('inf')

        left = 0
        freq = defaultdict(int)
        for right in range(len(cards)):
            freq[cards[right]] += 1
            while freq[cards[right]] >= 2:
                minm = min(minm, right-left+1)
                freq[cards[left]] -= 1
                left += 1

        return minm if minm != float('inf') else -1
