class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in range(len(rooms)):
            graph[i] = [num for num in rooms[i] if num != i]
        visited = set([0])
        queue = deque([0])

        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                visited.add(curr)
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return len(visited) ==  len(rooms)
        

        


        