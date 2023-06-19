import itertools 
array = [4, 6, 23, 10, 1, 3]

maximo = max(array)

sinMax = list(filter(lambda i: i!= maximo ,array))
decision = False

for i in range(2,len(sinMax)+1):
    combinations = list(itertools.combinations(sinMax, i))
    for j in combinations:
        if sum(j) == maximo:
            decision = True
            break

print(decision)


