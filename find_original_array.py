from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        
        count = Counter(changed)
        
        original = []
        for num in changed:
            if num in count and count[num] >= 1:
                count[num] -= 1
                if (num * 2) in count and count[(num * 2)] >= 1:
                    original.append(num)
                    count[num * 2] -= 1
            
            if len(original) == len(changed) // 2:
                return original
        
        return []
