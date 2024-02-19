class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            if nums[i] not in dicts:
                dicts[nums[i]] = [i]
            else:
                dicts[nums[i]].append(i)
        result = [0]*len(nums)
        for value in dicts.values():

            prefix_sum = [0,value[0]]
            for k in range(2,len(value)+1):
                prefix_sum.append(prefix_sum[k-1] + value[k-1])
            n = len(value)
            for j,idx in enumerate(value):
                result[idx] = idx*(2*j-n+1) - prefix_sum[j] + prefix_sum[-1] - prefix_sum[j+1]
                
        return result


        