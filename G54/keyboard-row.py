class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        for word in words:
            found = True
            temp = -1
            for char in word:
                if char.lower() in row1:
                    if temp != -1 and temp != 1:
                        found = False
                        break
                    else:
                        temp = 1
                if char.lower() in row2:
                    if temp != -1 and temp != 2:
                        found = False
                        break
                    else:
                        temp = 2
                if char.lower() in row3:
                    if temp != -1 and temp != 3:
                        found = False
                        break
                    else:
                        temp = 3
            if found:
                ans.append(word)
        return ans

        