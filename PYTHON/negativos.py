quantidade = int(input('Quantos números vc vai digitar: '))
lista_numeros = []
for i in range (quantidade):
    print('Digite um número: ')
    numero = int(input())
                    #posicao, numero
    lista_numeros.insert(i, numero)
for quant in lista_numeros:
    print(quant)
