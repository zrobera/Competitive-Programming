class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        scoreFirst = self.predictTheWinnerFrom(nums, 0, len(nums) - 1)
        scoreTotal = sum(nums)

        return scoreFirst >= scoreTotal - scoreFirst

    def predictTheWinnerFrom(self, nums: List[int], i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return nums[i]

        curScore = max(
            nums[i] + min(
                self.predictTheWinnerFrom(nums, i + 2, j),
                self.predictTheWinnerFrom(nums, i + 1, j - 1)
            ),
            nums[j] + min(
                self.predictTheWinnerFrom(nums, i, j - 2),
                self.predictTheWinnerFrom(nums, i + 1, j - 1)
            )
        )
        return curScore
