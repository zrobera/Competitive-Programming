class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if heights[i] < heights[j]:
                    names[i], names[j] = names[j],names[i]
                    heights[j], heights[i] =  heights[i],heights[j]
        return names