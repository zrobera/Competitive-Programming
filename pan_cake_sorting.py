class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)

        for i in range(n-1, -1, -1):
            max_idx = arr.index(max(arr[:i+1]))

            if max_idx != i:
                arr[:max_idx+1] = reversed(arr[:max_idx+1])
                flips.append(max_idx+1)

                arr[:i+1] = reversed(arr[:i+1])
                flips.append(i+1)

        return flips
