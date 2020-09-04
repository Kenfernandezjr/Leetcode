class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        def replace(s, char, i): 
            return s[:i] + char + s[i+1:]
        
        if len(palindrome) == 1:
            return ""
        
        for i in range(0, len(palindrome)//2):
            if palindrome[i] != "a":
                return replace(palindrome, "a", i)
            
        return replace(palindrome, "b", len(palindrome)-1)