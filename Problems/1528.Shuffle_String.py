class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # adding the variables
        tup = zip(*(indices, s))
        # in the tup variable i am creating a key/value tuple
        list2 = [0] * len(s) 
        # in the list i am creating a list with each element as 0
        # that will be replaced
        for k,v in tup:
        # this is the the for loop that will loop through each index of the tuple
          list2[k] = v
          # list2 will be getting the value placed at the index that is given by k
        return(''.join(list2))
        # the end i will be returning the list as a string by using the function join