class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)

        left = 0

        curr = defaultdict(int)
        anagrams = []
        for right in range(len(s)):
            curr[s[right]] += 1
            if right-left == len(p)-1:
                if curr == freq_p:
                    anagrams.append(left)    
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
        return anagrams


        