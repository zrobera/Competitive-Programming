class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s = set(fronts+backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in s:
                s.remove(fronts[i])
        return 0 if len(s) == 0 else s.pop()