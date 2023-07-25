class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(ip, pointer, dots):
            if dots > 4:
                return
            if dots == 4 and pointer >= len(s):
                ans.append(ip[:-1])
                return
            
            for length in range(1, 4):
                if pointer + length > len(s):
                    break
                num = s[pointer: pointer + length]
                
                if num[0] == '0' and length != 1:
                    break
                elif int(num) <= 255:
                    backtrack(ip + s[pointer: pointer + length] + ".", pointer + length, dots + 1)
        
        backtrack("", 0, 0)
        return ans
