class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        n= len(nums)
        i = 0
        while i < n*2:
            while stack and nums[stack[-1]] < nums[i%n]:
                ans[stack.pop()] = nums[i%n]
            stack.append(i%n)
            i += 1
        return ans
        