class Solution:
    def decodeString(self, s: str) -> str:
        closing_idx = 0
        stack = []
        idxs = defaultdict(int)
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(i-1)
            if s[i] == "]":
                idxs[stack.pop()] = i
        def helper(s,i):
            if not s:
                return ""
            if s[0].isnumeric():
                num = ""
                for j in range(len(s)):
                    num += s[j]
                    if not s[j+1].isnumeric():
                        break
                return int(num)*helper(s[j+1:],i+j+1)+ helper(s[idxs[i+j]+1-i:],idxs[i+j]+1)
            if s[0].isalpha():
                return s[0] + helper(s[1:],i+1)
            if s[0] == "]":
                return helper("", i+1)
            return helper(s[1:],i+1)
        ans = helper(s,0)
        return ans
        