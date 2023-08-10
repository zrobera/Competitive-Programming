#User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        cur = arr[i]
        par = arr[(i - 1) // 2]
        
        while i > 0 and par < cur:
            arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]
            i = (i - 1) // 2
            
            cur = arr[i]
            if i > 0:
                par = arr[(i - 1) // 2]
    
    # Function to build a Heap from an array.
    def buildHeap(self, arr, n):
        for i in range(1, n):
            self.heapify(arr, n, i)
    
    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        last = n
        
        while last > 0:
            arr[0], arr[last - 1] = arr[last - 1], arr[0]
            last -= 1
            
            ind = 0
            cur = arr[ind]
            c1 = c2 = -1
            
            if ind * 2 + 1 < last:
                c1 = arr[ind * 2 + 1]
            if ind * 2 + 2 < last:
                c2 = arr[ind * 2 + 2]
            
            while c1 > cur or c2 > cur:
                if c1 > cur and c1 > c2:
                    arr[ind * 2 + 1], arr[ind] = arr[ind], arr[ind * 2 + 1]
                    ind = ind * 2 + 1
                elif c2 > cur:
                    arr[ind * 2 + 2], arr[ind] = arr[ind], arr[ind * 2 + 2]
                    ind = ind * 2 + 2
                
                c1 = c2 = -1
                
                if ind * 2 + 1 < last:
                    c1 = arr[ind * 2 + 1]
                if ind * 2 + 2 < last:
                    c2 = arr[ind * 2 + 2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
