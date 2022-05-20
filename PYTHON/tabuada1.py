def exibirTabuada(numero):
                   #start, stop, step 
    for i in range(1,11,1):
        print(f'{numero} x {i} = {numero * i}')


numero = int(input('Você quer a tabuada de qual número? '))

exibirTabuada(numero)