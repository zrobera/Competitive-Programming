class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_time = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            x,y = ghost
            time = abs(target[0] -x) + abs(target[1] - y)
            if time <= player_time:
                return False
        return True

        