class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                right = i - stack[-1]
                curr = stack.pop()
                if stack:
                    left = curr - stack[-1]
                else:
                    left = curr + 1
                ans += arr[curr]*left*right
            stack.append(i)
        while stack:
            right = len(arr) - stack[-1]
            curr = stack.pop()
            if stack:
                left = curr - stack[-1]
            else:
                left = curr + 1
            ans += arr[curr]*left*right
        return ans%(10**9+7)
        