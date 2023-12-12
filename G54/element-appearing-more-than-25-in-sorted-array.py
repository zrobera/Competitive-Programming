class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = defaultdict(int)

        ans = -1
        for num in arr:
            freq[num] += 1
            if freq[num] > len(arr)/4:
                ans = num
                break
        return ans
        