class Solution:
    def isPalindrome(self, x: int) -> bool:
        finalNums = []
        for i in str(x):
            finalNums.append(i) 
        return finalNums == finalNums[::-1]
