def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        idx = 0
        for i in nums:
            for j in nums:
                if j< i:
                    arr[idx] += 1
            idx += 1
        return arr
