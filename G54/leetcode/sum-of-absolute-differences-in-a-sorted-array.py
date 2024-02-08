class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]

        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        result = []
        n = len(nums)
        for j in range(len(nums)):
            if j == 0:
                result.append(nums[j]*(2*j-n+1) + prefix_sum[-1] - prefix_sum[j])
            else:
                result.append(nums[j]*(2*j-n+1) - prefix_sum[j-1] + prefix_sum[-1] - prefix_sum[j])
        return result
