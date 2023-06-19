def letterCountI(str1):
    cont = 0
    arr = str1.split(" ")
    for i in arr:
        for j in i:
            ncont = i.count(j)
            if ncont > cont:
                cont = ncont
                palabra = i
                
    if cont <= 1:
        return print(-1)
    else:
        print(palabra)
       
                

str1 = " "
letterCountI(str1)