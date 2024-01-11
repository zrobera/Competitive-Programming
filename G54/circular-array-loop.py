class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            slow, fast = i, (i + nums[i]) % len(nums)

            while ( nums[slow] * nums[fast] > 0 and 
                    slow != (slow + nums[slow]) % len(nums) and 
                    nums[fast] * nums[(fast + nums[fast]) % len(nums)] > 0):
                if slow == fast:
                    return True

                slow = (slow + nums[slow]) % len(nums)
                fast = (fast + nums[fast]) % len(nums)
                fast = (fast + nums[fast]) % len(nums)

            j = i
            while nums[j] * nums[(j + nums[j]) % len(nums)] > 0:
                tmp = j
                j = (j + nums[j]) % len(nums)
                nums[tmp] = 0

        return False