class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = [[1]]
        for i in range(1,numRows):
            new_list = []
            for j in range(i+1):
                new_list.append(math.comb(i, j))
            lists.append(new_list)
        return lists