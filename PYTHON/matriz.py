'''
# inserindo elementos
# A matriz tem três linhas e três colunas
          #linha 1   # linha 2   # linha3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):  # 3-1 = 2
    for j in range(0, 3):
        elemento = int(input(f"Digite um elemento [{i}] [{j}]: "))
        matriz[i][j] = elemento
    

# exibir na tela
for i in range(3):
    for j in range(3):
        # :^5 centraliza os numeros e coloca 5 casas decimais
        print(f'[{matriz[i][j]:^5}]', end='') 
    print('')
    '''

matriz = [[0],[0,4]]
print(matriz[1][1])