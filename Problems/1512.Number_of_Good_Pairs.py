class Solution:
    ''' leader permutations and combinations '''
    def numIdenticalPairs(self, nums: List[int]) -> int:
        comb = combinations(nums, 2) 
        count = 0 
        for i, j in comb:
            ''' looping through the the pairs i created '''
            if i == j and i <= j:
                ''' if statment to return the count of each pair'''
                count +=1
        return(count)