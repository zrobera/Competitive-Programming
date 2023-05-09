class Solution:
    def kthLargestNumber(self,nums: List[str], k: int) -> str:
        numbers = list(map(int, nums ))
        numbers.sort(reverse = True)
        return str(numbers[k-1])
