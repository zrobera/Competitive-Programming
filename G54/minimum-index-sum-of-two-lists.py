class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minm = min(list1, list2, key = lambda x: len(x))
        maxm = list1 if minm == list2 else list2
        idxs = []
        ans = []
        least_idx = len(list1) + len(list2)
        for i, word1 in enumerate(minm):
            for j, word2 in enumerate(maxm):
                if word1 == word2:
                    print(word1, i, j)
                    least_idx = min(least_idx, i+j)
                    idxs.append((i+j, i))
        for sums, i in idxs:
            if sums == least_idx:
                ans.append(minm[i])     
        return ans

