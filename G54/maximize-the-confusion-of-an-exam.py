class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        count = {'T':0, 'F':0}
        ans = 0
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            while count['F'] > k and count['T'] > k:
                count[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
        