class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans = -1

        left, right = 0, 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                ans = nums1[left]
                break
        return ans
        