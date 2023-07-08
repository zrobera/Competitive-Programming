class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = [] 

        for i in range(len(nums)):
            if window and window[0] <= i - k:
                window.pop(0)

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result
        