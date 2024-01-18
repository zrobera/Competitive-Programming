class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        rem_freq = [1] + [0]*(k-1)
        for num in nums:
            prefix += num
            rem = prefix%k
            count += rem_freq[rem]
            rem_freq[rem] += 1
        return count
        

        
        