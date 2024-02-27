class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count = pow(5, (n + 1) // 2, 10**9 + 7)
        prime_count = pow(4, n // 2, 10**9 + 7)
        return (even_count * prime_count) % (10**9 + 7)