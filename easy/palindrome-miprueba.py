def palindrome(strp):
    pali = bool
    
    if len(strp) == 1:
        pali = True
    elif len(strp) == 2:
        pali = False
    else:  
        for i in range(1,len(strp)-1):
            if strp[i-1] == strp[i+1]:
                m = 2
                if len(strp) == 3:
                    pali = True
                    break
                while strp[i-m] == strp[i+m]:
                    m += 1 
                    if m > len(strp)/2:
                        break
      
        if m-1 == int((len(strp)/2)-0.5):
            pali = True
        else:
            pali = False
            
    return print(pali)
                


strp = 'abac'
palindrome(strp)