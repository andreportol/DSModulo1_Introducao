def fibonacci(limite):
    numeros = [0, 1]
    while(numeros[-1] < limite):
        numeros.append(sum(numeros[-2:]))
        #numeros.append(numeros[-2] + numeros[-1])
    return numeros

for num in fibonacci(10000):
    print(num)
