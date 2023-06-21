class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        pl1 = self.helper(nums, 0, len(nums) - 1)
        total = sum(nums)

        return pl1 >= total - pl1

    def helper(self, nums: List[int], i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return nums[i]

        curScore = max(
            nums[i] + min(
                self.helper(nums, i + 2, j),
                self.helper(nums, i + 1, j - 1)
            ),
            nums[j] + min(
                self.helper(nums, i, j - 2),
                self.helper(nums, i + 1, j - 1)
            )
        )
        return curScore
