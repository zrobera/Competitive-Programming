class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i , j = 0 , 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                start = max(firstList[i][0],secondList[j][0])
                end = min(firstList[i][1],secondList[j][1])
                ans.append([start,end])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                elif firstList[i][1] > secondList[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
        return ans