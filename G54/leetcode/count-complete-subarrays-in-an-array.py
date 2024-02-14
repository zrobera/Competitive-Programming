class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        completes = 0
        target = len(set(nums))

        left = 0
        curr = defaultdict(int)
        for right in range(len(nums)):
            curr[nums[right]] += 1
            while len(curr) == target:
                completes += len(nums) - right
                curr[nums[left]] -= 1
                if curr[nums[left]] == 0:
                    del curr[nums[left]]
                left += 1
        return completes