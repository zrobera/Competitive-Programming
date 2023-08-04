import heapq

class Solution:
    def largestInteger(self, num: int) -> int:
        evens = []
        odds = []
        num_str = str(num)
        for char in num_str:
            if int(char) % 2 == 0:
                heapq.heappush(evens, -int(char))  
            else:
                heapq.heappush(odds, -int(char))   
        
        ans = 0
        for char in num_str:
            if int(char) % 2 == 0:
                ans = ans * 10 - heapq.heappop(evens)
            else:
                ans = ans * 10 - heapq.heappop(odds)   
        return ans

        
