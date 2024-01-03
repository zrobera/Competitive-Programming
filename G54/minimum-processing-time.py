class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()

        j = len(tasks)-1
        ans = float('-inf')

        for time in processorTime:
           ans = max(ans, time + tasks[j])
           j -= 4
        return ans

            
        