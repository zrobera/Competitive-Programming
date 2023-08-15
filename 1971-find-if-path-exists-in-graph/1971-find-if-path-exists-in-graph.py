class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        queue = deque([source])
        
        while queue:
            current_node = queue.popleft()
            if current_node == destination:
                return True
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False
