from datetime import datetime

def countingMinutesI(strm):
    ind = strm.index("-")
    slice1 = strm[:ind]
    slice2 = strm[ind+1:]
    valor1 = datetime.strptime(slice1,"%I:%M%p")
    valor2 = datetime.strptime(slice2,"%I:%M%p")
    valor1_24h = valor1.strftime("%H:%M")
    valor2_24h = valor2.strftime("%H:%M")
    
    ind2 = valor1_24h.index(":")
    hora1 = int(valor1_24h[:ind2])
    min1 = int(valor1_24h[ind2+1:])
    
    ind3 = valor2_24h.index(":")
    hora2 = int(valor2_24h[:ind3])
    min2 = int(valor2_24h[ind3+1:])
    
    if hora1>hora2:
        resta1 = ((24-hora1)+hora2)*60
        if min2 > min1:
            restam = (min2 -min1)
            restaT = resta1 + restam
        elif min1 > min2:
            restam = min1 - min2
            restaT = resta1 - restam
        else: 
            restam = 0 
            restaT = resta1 + restam
    
    elif hora2>hora1: 
        resta1 = (hora2-hora1)*60
        if min2 > min1:
            restam = (min2 -min1)
        elif min1 > min2:
            restam = min1 - min2  
        else:
            restam = 0  
        restaT = resta1 + restam
    elif hora1 == hora2 and min1 != min2:
        if min2 > min1:
            resta1 = 0
            restam = (min2 -min1)
            restaT = resta1 + restam
        elif min1 > min2:
            resta1 = 24*60
            restam = min1 - min2  
            restaT = resta1 - restam
        else:
            restaT = 0
    else:
        restaT = 0
    
    
    return print(restaT)


strm = '11:20am-10:00am'
countingMinutesI(strm)

##OPCION 2 #### sumar horas con minutos y luego restar---más simple



