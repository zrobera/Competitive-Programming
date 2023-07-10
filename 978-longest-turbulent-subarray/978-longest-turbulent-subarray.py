class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        j =prev= cur = 0
        flip = False
        ans = 1
        all_equal = True
        def assignComp(x,y):
            if y > x:
                return 1
            elif y < x:
                return 2
            else:
                return 3

        for i in range(1, len(arr)):
            cur = assignComp(arr[i-1],arr[i])
            if cur == 3:
                j = i
                continue
            elif cur == prev:
                j = i-1
            elif cur != prev:
                flip = True
            prev = cur
            ans = max(ans, i-j+1)
        return ans if flip or prev == 0 else 2




        