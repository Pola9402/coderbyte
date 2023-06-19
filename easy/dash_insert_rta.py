def dashInsert(strd):
    arrstr = [int(ind) for ind in strd ]

    for i in range(0,len(arrstr)):
        if arrstr[i] == '-' or i == len(arrstr)-1:
            continue
        elif arrstr[i]%2 != 0 and arrstr[i+1]%2 != 0:
            arrstr.insert(i+1,'-')
        
    
    return print(arrstr)
   
strd = '123456789'
dashInsert(strd)
    
    