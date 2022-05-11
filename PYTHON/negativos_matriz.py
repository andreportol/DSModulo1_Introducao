linha = int(input('Qual a quantidade de linhas da matriz? '))
coluna = int(input('Qual a quantidade de colunas da matriz? '))
# criando a matriz
matriz = []
for _ in range(linha):
    matriz.append(['']*coluna) # Inserindo uma lista dentro da lista matriz e
    # repetindo a String '' na mesma quantidade da coluna'''

# inserindo dados na matriz
for l in range(linha):
    for c in range(coluna):
        elemento = int(input(f'Elemento [{l},{c}]: '))
        matriz[l][c] = elemento

# calculando valores negativos
print('VALORES NEGATIVOS:')
for l in range(linha):
    for c in range(coluna):
        if matriz[l][c] < 0:
            print(matriz[l][c])