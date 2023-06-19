def abCheck(strab):
    rta = bool
    
    if len(strab) < 5:
        rta = False
    else:    
        for i in range(0,len(strab)):
            if strab[i] == "a":
                if strab[i+4] == "b":
                    rta = True
                    break
                else:
                    rta = False
            else:
                if strab[i] == "b":
                    if strab[i+4] == "a":
                        rta = True
                        break
                    else:
                        rta = False
              
    return print(rta)

strab = "lane borrowed"
abCheck(strab)