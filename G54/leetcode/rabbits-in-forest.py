class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        same = 0
        curr = -1
        ans = 0

        for i in range(len(answers)):
            if answers[i] != curr or same <= 0:
                ans += answers[i] + 1
                same = answers[i]
                curr = answers[i]
            else:
                same -= 1
        return ans
