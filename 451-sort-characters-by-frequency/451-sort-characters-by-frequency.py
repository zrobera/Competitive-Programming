class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        sorted_string = ''
        for char in sorted_chars:
            sorted_string += char * freq[char]

        return sorted_string