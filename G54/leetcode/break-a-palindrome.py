class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        elif palindrome[0] != "a":
            return "a" + palindrome[1:]
        else:
            i = 0
            while (len(palindrome)%2 != 0 and i == len(palindrome)//2) or (i < len(palindrome) and palindrome[i] == "a"):
                i += 1
            if i >= len(palindrome):
                return palindrome[:len(palindrome)-1] + "b"
            else:
                return palindrome[:i] + "a" + palindrome[i+1:]
            
        