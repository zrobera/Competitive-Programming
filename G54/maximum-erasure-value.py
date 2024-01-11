class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        maxm = 0

        curr = 0
        freq = defaultdict(int)
        for right in range(len(nums)):
            curr += nums[right]
            freq[nums[right]] += 1
            while len(freq) < right-left+1:
                freq[nums[left]] -= 1
                curr -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            maxm = max(maxm, curr)

        return maxm
        