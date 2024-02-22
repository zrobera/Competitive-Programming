class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        score = 0
        i,j = 0, len(arr)-1
        while i < k-1:
            score -= arr[i]
            score += arr[j]
            i += 1
            j -= 1
        return score
        

        