class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        j = 0
        freq_p = {}
        freq_s = {}
        for char in p:
            if char not in freq_p:
                freq_p[char] = 0
            freq_p[char] += 1
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i],0) + 1
            if i-j+1 == len(p):
                if freq_p == freq_s:
                    ans.append(j)
                freq_s[s[j]] -= 1
                if freq_s[s[j]] == 0:
                    freq_s.pop(s[j])
                j += 1
        return ans

        

        