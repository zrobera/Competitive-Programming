class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                low = stack.pop()
                if stack:
                    length = min(height[stack[-1]],height[i])-height[low]
                    width = i - stack[-1]-1
                    area = width*length
                    ans += area
            stack.append(i)
        return ans
        