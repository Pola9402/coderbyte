def letterChanges(str1):
    arr = [i for i in str1]
    
    for i in range(0, len(arr)):
        if (ord(arr[i]) >= 65 and ord(arr[i]) <= 90) or (ord(arr[i]) >= 97 and ord(arr[i]) <= 122):
            arr[i] = ord(arr[i])
        
    for j in range(0,len(arr)):
        if arr[j] == 122 or arr[j] == 90:
            arr[j] = arr[j]-25
        elif type(arr[j]) == int:
            arr[j] = arr[j]+1
    
    for l in range (0, len(arr)):
        if type(arr[l]) == int:
            arr[l] =chr(arr[l])
        
    for k in  range (0, len(arr)):
        if arr[k] == "a" or arr[k] == "e" or arr[k] == "i" or arr[k] == "o" or arr[k] == "u":
            arr[k] = arr[k].upper()
            
    string = "".join(arr)
                    

    return print(string)

str1 = "QUICK brown FOX jumped OVER"
letterChanges(str1)