class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lists = []
        for num in range(1,n+1):
            if num%5 == 0 and num%3 == 0:
                lists.append("FizzBuzz")
            elif num%3 == 0:
                lists.append("Fizz")
            elif num%5 == 0:
                lists.append("Buzz")
            else:
                lists.append(str(num))
        return lists
