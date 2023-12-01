class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        maximum = max([word1,word2], key = lambda x: len(x))
        minimum = min([word1,word2], key = lambda x: len(x))
        ans += maximum[len(minimum):]
        return ans
        