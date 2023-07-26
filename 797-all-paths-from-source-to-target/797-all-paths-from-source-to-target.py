class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        candidate = [0]
        n = len(graph)
        def backtrack(candidate,i):
            if candidate[-1] == n-1:
                ans.append(candidate.copy())
                return

            for num in graph[i]:
                backtrack(candidate + [num], num)
        backtrack(candidate, 0)
        return ans


        