class Solution:
    def sortSentence(self, s: str) -> str:
        s_arr = s.split()

        arranged = [""]*len(s_arr)
        for word in s_arr:
            idx = int(word[-1])-1
            arranged[idx] = word[:-1]

        return " ".join(arranged)