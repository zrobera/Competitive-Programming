class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0]*(len(s)+1)

        for st,e,d in shifts:
            if d == 1:
                changes[st] += 1
                changes[e+1] -= 1
            else:
                changes[st] -= 1
                changes[e+1] += 1
        for i in range(1,len(changes)):
            changes[i] += changes[i-1]
        
        result = ""
        for j in range(len(s)):
            result += chr((ord(s[j]) - ord("a") + changes[j])%26 + ord("a"))
        
        return result


        