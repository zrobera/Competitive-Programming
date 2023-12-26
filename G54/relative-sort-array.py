class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dicts = Counter(arr1)
        ans = []
        for num in arr2:
            count = dicts[num]
            ans.extend([num]*count)
            del dicts[num]
        
        remain = []
        for num in dicts:
            remain.extend([num]*dicts[num])
        remain.sort()
        ans.extend(remain)
        return ans




        