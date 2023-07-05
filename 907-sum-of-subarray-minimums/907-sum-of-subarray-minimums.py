class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prv_stack = []
        nxt_stack = []
        size = len(arr)
        left = [0] * size
        right = [0] * size
        
        for i in range(size):
            while prv_stack and arr[prv_stack[-1]] > arr[i]:
                prv_stack.pop()
            left[i] = i + 1 if not prv_stack else i - prv_stack[-1]
            prv_stack.append(i)
        
        for i in range(size - 1, -1, -1):
            while nxt_stack and arr[nxt_stack[-1]] >= arr[i]:
                nxt_stack.pop()
            right[i] = size - i if not nxt_stack else nxt_stack[-1] - i
            nxt_stack.append(i)
        
        ans = 0
        mod = int(1e9) + 7
        for i in range(size):
            ans = (ans + arr[i] * left[i] * right[i]) % mod
        
        return ans
