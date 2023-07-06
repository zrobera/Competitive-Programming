class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums2.sort()
        for num in nums1:
            low, high = 0, len(nums2)-1
            while low <= high:
                mid = low + (high-low)//2
                if nums2[mid] == num:
                    ans.add(num) 
                    break
                elif nums2[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1                
        return list(ans)
        
        