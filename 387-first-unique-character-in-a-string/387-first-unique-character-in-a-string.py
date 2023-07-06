class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        for char in freq:
            if freq[char] == 1:
                return s.index(char)
        return -1

        