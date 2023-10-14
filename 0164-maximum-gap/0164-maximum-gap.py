class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_val, min_val = max(nums), min(nums)

        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        buckets = [None] * num_buckets
        for num in nums:
            index = (num - min_val) // bucket_size
            if buckets[index] is None:
                buckets[index] = [num, num]
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        prev_max = min_val
        for i in range(len(buckets)):
            if buckets[i] is not None:
                max_gap = max(max_gap, buckets[i][0] - prev_max)
                prev_max = buckets[i][1]

        return max_gap
        