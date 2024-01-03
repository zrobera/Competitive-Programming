class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()

        left, right = 0 , len(skill)-1
        sums = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != sums:
                return -1
            ans += (skill[left]*skill[right])
            left += 1
            right -= 1
        return ans
        