class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0]*len(nums)
        p = 1
        for i in range(len(nums)):
            product[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1):
            product[i] *= p
            p *= nums[i]
        return product
        