class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = j = 0
        count = {}
        ans = 0
        while i < len(s):
            if s[i] == "a":
                if "a" not in count:
                    count["a"] = 0
                count["a"] += 1
            elif s[i] == "b":
                if "b" not in count:
                    count["b"] = 0
                count["b"] += 1
            elif s[i] == "c":
                if "c" not in count:
                    count["c"] = 0
                count["c"] += 1
            if "a" in count and "b" in count and "c" in count:
                while count["a"] >= 1 and count["b"] >= 1 and count["c"] >= 1:
                    ans += len(s)-i
                    count[s[j]] -= 1
                    j += 1
            i += 1

        return ans

