class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans =  True
        while n >=1:
            rem = n % 3
            if rem == 2:
                ans = False
                break
            n//= 3
        return ans
                
        