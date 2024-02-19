class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_sum = [0]*(len(customers)+1)
        for i in range(len(customers)):
            if customers[i] == "Y":
                prefix_sum[i+1] = prefix_sum[i] + 1
            else:
                prefix_sum[i+1] = prefix_sum[i]

        minm = len(customers)+1
        ans = len(customers)
        for j in range(len(customers)):
            penality = (j-prefix_sum[j]) + prefix_sum[-1] - prefix_sum[j]
            if penality < minm:
                ans = j
                minm = penality
        if len(customers) - prefix_sum[-1] < minm:
            ans = len(customers)
        return ans
            
