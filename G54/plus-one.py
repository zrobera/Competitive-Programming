class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = map(str, digits)
        number = "".join(digits_str)
        large_int = str(int(number) + 1)

        int_as_list = list(large_int)
        ans = list(map(int, int_as_list))
        return ans
        



        