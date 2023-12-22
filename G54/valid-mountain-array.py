class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        up = True if arr[1] > arr[0] else False
        changed = False
        for i in range(1,len(arr)-1):
            if arr[i] == arr[i+1] or (arr[i-1] > arr[i] and arr[i+1] > arr[i]):
                return False
            if (up and arr[i] > arr[i+1]) or (not up and arr[i] < arr[i+1]):
                changed = True

        return True if changed else False
            


        