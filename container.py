class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        max_vol = 0
        while i < j:
            max_vol = max(max_vol, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_vol
