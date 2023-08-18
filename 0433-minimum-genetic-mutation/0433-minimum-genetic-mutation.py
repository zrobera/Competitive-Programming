class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene,0)])
        valid = set(bank)

        while queue:
            cur,count = queue.popleft()
            if cur == endGene:
                return count
            for i in range(8):
                for char in "ACGT":
                    new = cur[:i] + char + cur[i+1:]
                    if new in valid:
                        valid.remove(new)
                        queue.append((new, count+1))
        return -1

