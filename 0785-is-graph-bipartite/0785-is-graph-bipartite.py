class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        def isPossible(graph, colors, color, node):
            if colors[node] != 0:
                return colors[node] == color
            colors[node] = color
            for nbr in graph[node]:
                if not isPossible(graph, colors, -color, nbr):
                    return False
            return True
        
        for i in range(len(graph)):
            if colors[i] == 0 and not isPossible(graph, colors, 1, i):
                return False
        return True
