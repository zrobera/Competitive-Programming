class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        ans = []
        maxm = len( max(arr, key = lambda x: len(x)))
        for i in range(maxm):
            temp = ""
            for word in arr:
                if i < len(word):
                    temp += word[i]
                else:
                    temp += " "
            ans.append( temp.rstrip())
        return ans


                

        