class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if len(matrix) == 0:
            return ans
        rs = 0
        re = len(matrix) - 1
        cb = 0
        ce = len(matrix[0]) - 1
        while rs <= re and cb <= ce:
            for j in range(cb, ce + 1):
                ans.append(matrix[rs][j])
            rs += 1
            
            for j in range(rs, re + 1):
                ans.append(matrix[j][ce])
            ce -= 1
            
            if rs <= re:
                for j in range(ce, cb - 1, -1):
                    ans.append(matrix[re][j])
            re -= 1
            
            if cb <= ce:
                for j in range(re, rs - 1, -1):
                    ans.append(matrix[j][cb])
            cb += 1
        
        return ans
