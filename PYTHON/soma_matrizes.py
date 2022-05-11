linha = int(input('Quantas linhas vai ter cada matriz? '))
coluna = int(input('Quantas colunas vai ter cada matriz? '))

# inicializando as matrizes
matriz_A = []
matriz_B = []
matriz_Soma = []

for _ in range(linha):
   matriz_A.append(['']*coluna)
   matriz_B.append(['']*coluna)
   matriz_Soma.append(['']*coluna)
# inserindo dados na matriz A
for l in range(linha):
    for c in range(coluna):
        elemento = int(input(f'Elemento [{l},{c}]: '))
        matriz_A[l][c] = elemento
# inserindo dados na matriz B
for l in range(linha):
    for c in range(coluna):
        elemento = int(input(f'Elemento [{l},{c}]: '))
        matriz_B[l][c] = elemento

#Somando as matrizes A e B
for l in range(linha):
    for c in range(coluna):
        matriz_Soma[l][c] = matriz_A[l][c] + matriz_B[l][c]
    
# exibindo matriz soma
print('Matriz Soma:')
for mat_s in matriz_Soma:
   print(f'{mat_s}',end='\n')

# exibindo matriz soma alinhada
print()
print('Matriz Soma: ')
for l in range(linha):
    for c in range(coluna):
        print(f'{matriz_Soma[l][c]:^5}', end=' ')
    print()
