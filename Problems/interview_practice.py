# write a function that returns a boolean 

s = ""
left = 0
right = len(s) - 1
t =[]
while left < right:
  if s[left].casefold() == s[right].casefold():
    t.append(True)
    left = left + 1
    right = right - 1
  elif s[left].isalpha() == False: 
    left = left + 1 
  elif s[right].isalpha() == False: 
    right = right - 1
  else:
    t.append(False)
    break
print(all(t)) 