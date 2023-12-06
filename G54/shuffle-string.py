class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = "a"*len(s)
        for i,index in enumerate(indices):
            ans = ans[:index] + s[i] + ans[index+1:]
        return ans