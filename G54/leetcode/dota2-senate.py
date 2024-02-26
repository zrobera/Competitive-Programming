class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_d = deque()
        queue_r = deque()
        for i,char in enumerate(senate):
            if char == "D":
                queue_d.append(i)
            else:
                queue_r.append(i)
        while True:
            for i in range(len(senate)):
                if not queue_r:
                    return "Dire"
                if not queue_d:
                    return "Radiant"
                elif senate[i] == "D" and queue_d[0] == i:
                    queue_r.popleft()
                    poped = queue_d.popleft()
                    queue_d.append(poped)
                elif senate[i] == "R" and queue_r[0] == i:
                    queue_d.popleft()
                    poped = queue_r.popleft()
                    queue_r.append(poped)
                