def firstFactorial(num1):
    valor = 1
    for i in range (num1,0,-1):
        valor *= i
        num1 += 1
    return print(valor)

num1 = 18
firstFactorial(num1)