class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minm = len(nums)//3
        freq = {}
        ans = set()
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            if freq[num] > minm:
                ans.add(num)
        return list(ans)
