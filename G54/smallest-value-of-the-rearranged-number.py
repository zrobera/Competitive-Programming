class Solution:
    def smallestNumber(self, num: int) -> int:
        positive = True
        if num < 0:
            positive = False
            num = abs(num)
        arr = []
        zeros = 0
        while num > 0:
            last = num%10
            if last != 0:
                arr.append(last)
            else:
                zeros += 1
            num = num//10
        if not positive:
            arr.sort(reverse = True)
        else:
            arr.sort()
        
        ans = 0
        multiplier = len(arr)+zeros-1

        for i in range(len(arr)):
            ans += arr[i] * (10**multiplier)
            if positive and i == 0:
                multiplier -= zeros+1
            else:
                multiplier -= 1
        
        return ans if positive else -1*ans

        