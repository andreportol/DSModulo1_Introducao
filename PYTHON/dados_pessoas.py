# variaveis
quantidade = int(input('Quantas pessoas serão digitadas: '))
alturas = []
alturasMulheres = []
generos = []
# inserindo dados nos vetores
for i in range(quantidade):
    altura = float(input(f'Altura da {i+1}º pessoa: '))
    genero = input(f'Gênero da {i+1}º pessoa: ')
    alturas.append(altura)
    generos.append(genero)
    if generos[i] == 'F':
        alturasMulheres.insert(i, altura)
# Exibindo a menor e a maior altura
print(f'Menor altura: {min(alturas)}')
print(f'Maior altura: {max(alturas)}')

# Calculando a média de altura das mulheres
'''
soma = 0
for i in range(len(alturasMulheres)):
    soma = soma + alturasMulheres[i]
tamanho = len(alturasMulheres)
mediaAlturaMulheres = soma / tamanho
print(f'Media de altura das mulheres: {mediaAlturaMulheres}')
'''
soma = sum(alturasMulheres)
tamanhoVetor = len(alturasMulheres)
mediaAlturaMulheres = soma / tamanhoVetor
print(f'Media de altura das mulheres: {mediaAlturaMulheres}')

# calculando o numero de homens
contadorHomens = 0
for i in range(quantidade):
    if generos[i] == 'M':
        contadorHomens += 1
print(f'Quantidade de homens: {contadorHomens}')


