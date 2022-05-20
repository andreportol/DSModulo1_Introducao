def imc(peso, altura):
    imc = peso/(altura * altura)
    return imc

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
print(f'IMC = {imc(peso, altura):.2f}')
