import string

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        list = []
        for i in word:
            if i in string.ascii_uppercase:
                list.append(True)
            if i in string.ascii_lowercase:
                list.append(False)
  
        if all(list):
            return(True)
        elif not any(list):
            return(True)
        elif list[0] == True and any(list[1:]) is False:
            return(True)
        else:
            return(False)