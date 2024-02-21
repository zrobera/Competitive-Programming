class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicts = defaultdict()
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                dicts[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = [-1]*len(nums1)    

        for i in range(len(nums1)):
            if nums1[i] in dicts:
                ans[i] = dicts[nums1[i]]
        return ans

