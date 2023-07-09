class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p_dict = Counter(p)
        l = 0
        r = len(p)

        while r <= len(s):
            window = s[l:r]
            window = Counter(window)

            if window == p_dict:
                ans.append(l)

            r+=1
            l+=1
        return ans
        

        