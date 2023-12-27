class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        freq = Counter(nums1)

        for num in nums2:
            if freq[num] > 0:
                ans.append(num)
                freq[num] -= 1
        
        return ans





        