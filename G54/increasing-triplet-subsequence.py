class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dictionary = defaultdict(list)
        minm = float('inf')
        for i in range(len(nums)):
            dictionary[i].append(minm)
            minm = min(minm,nums[i])
        maxm = float('-inf')
        for j in range(len(nums)-1,-1,-1):
            dictionary[j].append(maxm)
            maxm = max(maxm,nums[j])

        for k in range(len(nums)):
            if dictionary[k][0] < nums[k] < dictionary[k][1]:
                return True
        return False

        