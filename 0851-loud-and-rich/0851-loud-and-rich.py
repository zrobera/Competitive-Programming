class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph =  defaultdict(list)
        n= len(quiet)
        ans = [-1 for _ in range(n)]

        for i,j in richer:
            graph[j].append(i)

        def dfs(curr):
            if ans[curr] == -1:
                ans[curr] = curr
                for neighbor  in graph[curr]:
                    least = dfs(neighbor)
                    if quiet[least] < quiet[ans[curr]]:
                        ans[curr] = least
            return ans[curr]
        for i in range(n):
            if ans[i] == -1:
                dfs(i)
        return ans