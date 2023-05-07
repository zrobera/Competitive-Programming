class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        else:
            next_start = (k - 1) % n + 1
            winner = self.findTheWinner(n - 1, k)
            return (winner + next_start - 1) % n + 1
