class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverser(left: int, right: int) -> None:
            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            reverser(left + 1, right - 1)
        
        reverser(0, len(s) - 1)
