class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo,hi = 0, len(letters)-1
        while lo < hi:
            mid = (lo+hi)//2
            if ord(letters[mid]) <= ord(target):
                lo = mid + 1
            else:
                hi = mid
        return letters[lo] if ord(letters[lo]) > ord(target) else letters[0]
        