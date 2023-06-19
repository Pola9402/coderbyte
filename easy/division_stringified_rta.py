def divisionStringified(num1,num2):
    
    if num2 == 0:
        rta = 'undefined'
    else:
        div = list(reversed(str(int(num1/num2))))
        arr = [int(dig) for dig in div]
        if len(arr)>3:
            cont = 0
            m = 1
            for i in range(0,len(arr)):
                cont += 1
                if cont == 3:
                    arr.insert(i+m,",")
                    cont = 0
                    m += 1
            cadena =''.join(map(str, arr))
            rta = cadena[::-1]    
        else:
            cad = ''.join(map(str, arr))
            rta = cad[::-1]
    
    return print(rta)

num1 = 999999
num2 = 0
divisionStringified(num1,num2)