class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1]*len(nums)

        stack = []

        for i in range(2*len(nums)):
            i %= len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                poped = stack.pop()
                answer[poped] = nums[i]
            stack.append(i)
        return answer