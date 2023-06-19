def longestWord(sen):
    worte = ""
    cont = 0
    myDict = {}
    arr = []
    
    for i in sen:
        if (ord(i)>65 and ord(i)<90) or (ord(i)>97 and ord(i)<122):
            worte += i
        else:
            worte += ","
    
    arr = worte.split(",")
    
    for j in arr:
        for k in j:
            cont += 1
        myDict[j] =cont
           
        cont = 0
        
    maximo = max(list(myDict.values()))
    
    for clave, valor in myDict.items():
        if valor == maximo:
            return print(clave)
            
        
     

sen = 'the$%!#$.quick*brown fox jump*!#$!@$!$!!%!00an'
longestWord(sen)

