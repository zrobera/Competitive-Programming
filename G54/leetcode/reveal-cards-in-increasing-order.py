class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0]*len(deck)

        i, j = 0,0
        empties = []
        while i < len(deck):
            if i+1 < len(deck):
                empties.append(i+1)
            ans[i] = deck[j]
            j += 1
            i += 2

        k = len(deck)%2
        
        while j < len(deck)-1:
            ans[empties[k]] = deck[j]
            del empties[k]
            k = (k+1)%len(empties)
            j += 1
        if empties:
            ans[empties[0]] = deck[j] 
        return ans

        
        
