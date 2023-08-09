class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        prev_end = -1
        furthest_end, ans = 0 , 0
        for start, end in clips:
            if furthest_end >= time:
                return ans
            if start > furthest_end:
                return -1
            if start <= prev_end:
                furthest_end = max(furthest_end,end)
            else:
                prev_end = furthest_end
                furthest_end = max(furthest_end,end)
                ans += 1
        return ans if furthest_end >= time else -1