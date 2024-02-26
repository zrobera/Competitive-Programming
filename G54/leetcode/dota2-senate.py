class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_d = deque()
        queue_r = deque()
        for i,char in enumerate(senate):
            if char == "D":
                queue_d.append(i)
            else:
                queue_r.append(i)
        n = len(senate)
        while queue_r and queue_d:
            if queue_d[0] < queue_r[0]:
                queue_r.popleft()
                poped = queue_d.popleft()
                queue_d.append(poped+n)
            else:
                queue_d.popleft()
                poped = queue_r.popleft()
                queue_r.append(poped+n)
        return "Radiant" if queue_r else "Dire"