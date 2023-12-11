class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]

        losses = {}

        for match in matches:
            losses[match[1]] = losses.get(match[1], 0) + 1
            if match[0] not in losses:
                losses[match[0]] = 0
                
        for key in losses:
            if losses[key] == 0:
                ans[0].append(key)
            elif losses[key] == 1:
                ans[1].append(key)
                
        ans[0].sort()
        ans[1].sort()
        return ans
            
                    

        
        