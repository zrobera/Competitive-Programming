def countingSort(arr):
    # Write your code here
    frequency_arr = [0]*100
    for i in arr:
        frequency_arr[i] += 1
    return frequency_arr
