class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        minimum = len(min(words, key = lambda x: len(x)))
        i = 0
        for j in range(len(words)-1):
            word = words[j]
            breaked = False
            while i < min(len(word), len(words[j+1])):
                if j+1 < len(words) and len(words[j+1]) >= i and order.index(word[i]) < order.index(words[j+1][i]):
                    breaked = True
                    break

                elif j+1 < len(words) and len(words[j+1]) >= i and order.index(word[i]) > order.index(words[j+1][i]):
                    return False
                i += 1  
            if not breaked and len(word) > len(words[j+1]):
                return False 
        return True


        