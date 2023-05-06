class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        i = len(citations)-1
        j = 1
        while i >= 0:
            if citations[i] < j:
                break
            ans += 1
            j += 1
            i -= 1
        return ans 
        
