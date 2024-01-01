class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        
        for i in range(len(arr)):
            max_ = max(arr[:len(arr) - i])
            max_i = arr.index(max_) + 1
            arr[:max_i] = arr[:max_i][::-1]
            flips.append(max_i)
            
            arr[:len(arr) - i] = arr[:len(arr) - i][::-1]
            flips.append(len(arr) - i)
        return flips


        