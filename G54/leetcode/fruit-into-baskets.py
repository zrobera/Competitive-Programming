class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0

        count = 0
        types = defaultdict(int)
        for right in range(len(fruits)):
            types[fruits[right]] += 1
            while len(types) > 2:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left += 1
            
            count = max(count, right-left+1)
        return count
        