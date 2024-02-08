class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        changes = [0]*len(nums)

        for start,end in requests:
            changes[start] += 1
            if end < len(nums)-1:
                changes[end+1] -= 1
   
        for i in range(1,len(changes)):
            changes[i] += changes[i-1]
        
        indexes = [ j for j in range(len(nums))]
        
        indexes.sort(key = lambda x: changes[x], reverse = True)
        
        nums.sort(reverse = True)
        new_nums = [0]*len(nums)
        for k in range(len(nums)):
            new_nums[indexes[k]] = nums[k]
        
        prefix_sum = [new_nums[0]]
        for l in range(1,len(nums)):
            prefix_sum.append(prefix_sum[l-1] + new_nums[l])
        ans = 0
        for st,en in requests:
            if st == 0:
                ans += prefix_sum[en]
            else:
                ans += (prefix_sum[en] - prefix_sum[st-1])
        return ans%(10**9+7)
        