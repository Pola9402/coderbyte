array = []

if len(array)>2:
    for i in range(1, len(array)-1):
        if array[i] - array[i-1] == array[i+1] - array[i]:
            var = "arithmetic"
        elif array[i] / array[i-1] == array[i+1] / array[i]:
            var = "geometric"
        else:
            var = -1
else:
    var = -1
    

print(var)
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    