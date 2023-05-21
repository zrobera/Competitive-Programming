class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert_reverse(s):
            inverted = "".join(["0" if char == "1" else "1" for char in s])
            return inverted[::-1]
        def kth_str(n):
            if n<=1: return "0"
            return kth_str(n-1)+"1"+invert_reverse(kth_str(n-1))
        return kth_str(n)[k-1]
        
