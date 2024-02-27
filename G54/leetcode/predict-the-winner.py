class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums, i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i]

            curScore = max(
                nums[i] + min(helper(nums, i + 2, j),helper(nums, i + 1, j - 1)),
                nums[j] + min(helper(nums, i, j - 2),helper(nums, i + 1, j - 1))
            )
            return curScore
        player1 = helper(nums, 0, len(nums) - 1)
        player2 = sum(nums) - player1

        return player1 >= player2