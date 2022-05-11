# criando uma matriz
matriz = []
ordem = int(input('Qual a ordem da matriz? '))
for _ in range(ordem):
    matriz.append([''] * ordem)
# [''] * ordem     é igual ao numero de vezes que 
# o elemento da lista vai repetir


# inserindo dados na matriz
for l in range(ordem):
    for c in range(ordem):
        elemento = int(input(f'Elemento [{l},{c}]:'))
        matriz[l][c] = elemento

# calculando dados matriz

# repete o elemento do vetor dentro da propria lista
# a mesma quantidade de vezes do valor da ordem
vetor = [0] * ordem
# ordem = 3
# vetor[0, 0, 0]
print(vetor)
for l in range(ordem):
    for c in range(ordem):
        if matriz[l][c] > vetor[l]:
            vetor[l] = matriz[l][c]

# exibindo os dados
for i, vec in enumerate(vetor):
    print(f'O maior elemento da linha {i} = {vec}', end='\n')
