list_nome = []
list_nota1 = []
list_nota2 = []
list_aprovados = []
list_media = []
list_reprovados = []
def exibirTabela():
    for i in range (len(list_nome)):
        media = (list_nota1[i] + list_nota2[i])/2
        print(f'{list_nome[i]},{list_nota1[i]},{list_nota2[i]}, MEDIA = {media}')

def exibirPessoasAprovadas():
    for p in range (len(list_nome)):
        media = (list_nota1[p] + list_nota2[p])/ 2
        if media >= 70:
            list_aprovados.append(list_nome[p])
            list_media.append(media)
        else:
            list_reprovados.append(list_nome[p])
    if len(list_aprovados) != 0:
        print('PESSOAS APROVADAS:')
        for aprovados in list_aprovados:
            print(aprovados)
    else: 
        print('Não há aprovados')

def exibirPorcentagemAprovacao():
    if len(list_aprovados) != 0:
        aprovacao = len(list_aprovados) / len (list_nome)
        print(f'Porcentagem de aprovação: {aprovacao * 100 :.1f}%')
    else:
        print('Porcentagem de aprovação = 0.00%')

def calcularMaiorMedia():
    if len(list_media) != 0:
        maiorValor_Media = max(list_media)
        indice = list_media.index(maiorValor_Media)
        print(f'Maior média: {list_aprovados[indice]}')
    else:
        maiorValor_Reprovados = max(list_reprovados)
        indice = list_reprovados.index(maiorValor_Reprovados)
        print(f'Maior média: {list_reprovados[indice]}')

def calcularMediaAprovados():
    if len(list_aprovados) != 0:
        soma = sum(list_media)
        quantidade = len(list_media)
        mediaAprovados = soma / quantidade
        print(f'Nota média dos aprovados: {mediaAprovados:.2f}')
    else:
        print('Não ha canditados aprovados!')

def main():
    if __name__ == '__main__':
        quant_pessoas = int(input('Qual a quantidade de pessoas?'))
        for p in range(quant_pessoas):
            print(f'Digite os dados da {p+1}º pessoa: ')
            nome = input('Nome: ')
            list_nome.append(nome)
            nota1 = float(input(f'Nota etapa 1: '))
            list_nota1.append(nota1)
            nota2 = float(input(f'Nota etapa 2: '))
            list_nota2.append(nota2)

main()
exibirTabela()
exibirPessoasAprovadas()
exibirPorcentagemAprovacao()
calcularMaiorMedia()
calcularMediaAprovados()
    
