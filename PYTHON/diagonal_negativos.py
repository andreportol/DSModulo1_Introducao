# criando uma lista
matriz = []

ordem_matriz = int(input("Qual a ordem da matriz: "))

# criando listas dentro da lista matriz
for i in range(ordem_matriz):
    matriz.append([i] * ordem_matriz) # cria uma lista dentro da lista matriz
# exemplo: se ordem_matriz = 3 repete o elemento da lista tres vezes
# matriz = [[0,0,0],[1,1,1],[2,2,2]]


# inserindo elementos dentro da matriz
for i in range(ordem_matriz):
    for j in range(ordem_matriz):
        elemento = int(input(f'Elemento [{i}] [{j}]: '))
        matriz[i][j] = elemento

# exibe a diagonal principal
print('DIAGONAL PRINCIPAL:')
for i in range(ordem_matriz):
    for j in range(ordem_matriz):
        if i == j:
            print(matriz[i][j], end=' ')   
print()
# exibindo números negativos
contador_negativos = 0
for i in range(ordem_matriz):
    for j in range(ordem_matriz):
        if matriz[i][j] < 0:
            contador_negativos += 1
print(f'QUANTIDADE DE NEGATIVOS: {contador_negativos}')
# exibindo a matriz
'''
for m in matriz:
    print(m)
'''
