class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        count = {}
        removed_nums = 0
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_count = sorted(count.values(), reverse=True)
        total_count = 0
        i = 0
        while total_count < size // 2:
            total_count += sorted_count[i]
            removed_nums += 1
            i += 1
        return removed_nums
