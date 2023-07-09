class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans,j = 0,0
        types_left = 2
        freq = {f: 0 for f in fruits}
        
        for i in range(len(fruits)):
            freq[fruits[i]] += 1
            if freq[fruits[i]] == 1:
                types_left -= 1
            if types_left < 0:
                freq[fruits[j]] -= 1
                if freq[fruits[j]] == 0:
                    types_left += 1
                j += 1
            ans = max(ans, i-j+1)
        return ans

        