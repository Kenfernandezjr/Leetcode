class Solution:
    def defangIPaddr(self, address: str) -> str:
        # completed this 3 different ways
        # First
        changeList = list(address)
        for i in range(len(changeList)):
            if changeList[i] is ".":
                changeList[i] = "[.]"
        return("".join(changeList))
        
        # Second
        return "".join(["[.]" if i is "." else i for i in list(address)])

        # Third
        return address.replace(".", "[.]")
        

