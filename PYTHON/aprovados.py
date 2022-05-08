# vetores
nomes = []
notas1 = []
notas2 = []
medias = []
# inserindo dados nos vetores
quantidade = int(input('Quantos alunos serão digitados: '))
for i in range(quantidade):
    print(f'Digite nome, primeira e segunda nota do {i+1} aluno: ')
    nome = input()
    nota1 = float(input())
    nota2 = float(input())
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)

# calculando a media das notas
print('Alunos aprovados:')
for i in range(quantidade):
    medias.append((notas1[i] + notas2[i]) / 2)
    if medias[i] >= 6:
        print(nomes[i], end='\n')
    
