class Solution:
    def interpret(self, command: str) -> str:
        temp = ""
        ans = ""
        for char in command:
            if char == "G":
                ans += "G"
            else:
                temp += char
            if temp == "()":
                ans += "o"
            elif temp == "(al)":
                ans += "al"
            if temp and temp[-1] == ")":
                temp = ""
        return ans
            
        