class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def divider(k):
            
            if k == 1:
                return True
                      
            if k % 3 != 0:
                return False
            
            if k < 3:
                return False
            
            return divider(k//3)
        
        return divider(n)