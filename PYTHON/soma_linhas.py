linhas = int(input('Qual a quantidade de linhas da matriz? '))
colunas = int(input('Qual a quantidade de colunas da matriz? '))
lista = []
vetor_soma = []
# criando a matriz
for _ in range(linhas):
    lista.append([''] * colunas)

# inserindo dados dentro da lista
for i in range(linhas):
    print(f'Digite os elementos da {i+1}º linha: ')
    for j in range(colunas):
        elemento = int(input())
        lista[i][j] = elemento

# calculando vetor gerado
for i in range(linhas):
    vetor_soma.append(0)
    for j in range(colunas):
        vetor_soma[i] = vetor_soma[i] + lista[i][j]

# exibindo vetor
print('VETOR GERADO: ')
for i in range(linhas):
    print(vetor_soma[i])
