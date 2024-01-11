class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0

        even_idx = {}
        last_even = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]%2 == 0:
                last_even = max(last_even, i)
            else:
                even_idx[i] = last_even
                last_even = -1
                
        left = 0
        odds = 0
        for right in range(len(nums)):
            if nums[right]%2 != 0:
                odds += 1
            while odds == k:
                if even_idx[right] == -1:
                    count += 1
                else:
                    count += even_idx[right]-right+1
                if nums[left]%2 != 0:
                    odds -= 1
                left += 1
        return count
