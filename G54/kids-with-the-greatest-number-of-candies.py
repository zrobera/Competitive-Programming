class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxm = max(candies)
        ans = []
        for candy in candies:
            current = candy + extraCandies
            ans.append(current >= maxm)
        return ans

        