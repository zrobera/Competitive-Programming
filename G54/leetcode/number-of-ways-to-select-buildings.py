class Solution:
    def numberOfWays(self, s: str) -> int:
        nums1 = s.count("1")
        nums0 = len(s) - nums1

        count0 = 0
        count1 = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "1":
                ans += (count0*(nums0-count0))
                count1 += 1
            else:
                ans += (count1*(nums1-count1))
                count0 += 1
        return ans
