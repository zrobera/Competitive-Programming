class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i,j = 0, 0
        ans = []

        up = True
        while len(ans) < len(mat)*len(mat[0]):
            ans.append(mat[i][j])
            if up:
                i -= 1
                j += 1
                if i < 0 and j < len(mat[0]):
                    i = 0
                    up = not up
                elif j > len(mat[0])-1:
                    j = len(mat[0])-1
                    i += 2
                    up = not up
            else:
                i += 1
                j -= 1

                if j < 0 and i < len(mat):
                    j = 0
                    up = not up
                elif i > len(mat)-1:
                    i = len(mat)-1
                    j += 2
                    up = not up
        return ans





        