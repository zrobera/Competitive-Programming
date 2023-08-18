class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] ==1:
                    graph[i].append(j)
        def dfs(node,visited):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour,visited)
            return True

        visited = set()
        count = 0
        for node in graph:
            count += dfs(node,visited)
                
        return count