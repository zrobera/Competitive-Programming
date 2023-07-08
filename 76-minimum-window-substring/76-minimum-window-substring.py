class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters_needed = {} 
        i,j = 0, 0
        missing = 0
        min_str = [float("-inf"), float("inf")]
        for char in t:
            if char in letters_needed:
                letters_needed[char] += 1
            else:
                letters_needed[char] = 1
                missing += 1
        for i in range(len(s)):
            if s[i] in letters_needed:
                letters_needed[s[i]] -= 1
                if letters_needed[s[i]] == 0:
                    missing -= 1
            while missing == 0:
                if i - j < (min_str[1] - min_str[0]):
                    min_str[1] = i
                    min_str[0] = j
                if s[j] in letters_needed:
                    letters_needed[s[j]] += 1
                    if letters_needed[s[j]] > 0:
                        missing += 1
                j += 1
        return "" if min_str[0] == float("-inf") else s[min_str[0]:min_str[1]+1]
                