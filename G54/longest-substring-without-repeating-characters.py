class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr= defaultdict(int)

        left = 0
        ans = 0
        for right in range(len(s)):
            curr[s[right]] += 1
            while curr[s[right]] > 1:
                curr[s[left]] -= 1
                left += 1

            ans = max(ans, right-left+1)
        
        return ans
            
            

        