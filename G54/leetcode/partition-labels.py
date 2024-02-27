class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dicts = defaultdict(int)
        for i,char in enumerate(s):
            dicts[char] = i
        curr = dicts[s[0]]
        partitions = []
        size = 0
        for i,char in enumerate(s):
            if i > curr:
                curr = dicts[char]
                partitions.append(size)
                size = 0
            curr = max(curr, dicts[char])
            size += 1
        partitions.append(size)
        return partitions

        