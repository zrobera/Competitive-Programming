class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evens = 0
        for num in nums:
            if num % 2 == 0:
                evens += num
        for val,idx in queries:
            temp = nums[idx]
            if nums[idx] % 2 == 0:
                evens -= temp
            nums[idx] += val
            if nums[idx] % 2 == 0:
                evens += nums[idx]
            ans.append(evens)
        return ans
            

        