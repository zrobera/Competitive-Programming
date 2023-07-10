class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low ,high = 0, len(arr)-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid-1

        R = low 
        L = R - 1  
        while k > 0:
            if R >= len(arr) or (L >= 0 and x - arr[L] <= arr[R] - x):
                L -= 1
            else:
                R += 1
            k -= 1    
        return arr[L + 1:R]
    
        
