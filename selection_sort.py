class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if arr[j]< arr[min]:
                    min = j
            if min != i:
                arr[i], arr[min] = arr[min], arr[i]
                
        return arr
