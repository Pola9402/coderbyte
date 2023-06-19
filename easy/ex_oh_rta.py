def exOh(str1):
  cont1 = 0
  cont2 = 0
  
  for i in str1:
    if i == "x":
      cont1 +=1
    elif i == "o":
      cont2 += 1
  
  if cont1 == cont2:
    return print(True)
  else:
    return print(False)
      

str1 = "oooxxoooxxxx"
exOh(str1)


