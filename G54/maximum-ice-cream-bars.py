class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maximum = max(costs)
        arr = [0]*(maximum+1)
        for cost in costs:
            arr[cost] += 1

        count = 0
        for i in range(len(arr)):
            if i > coins:
                break
            num = arr[i]
            while num > 0 and i <= coins:
                coins -= i
                num -= 1
                count += 1
        return count


        