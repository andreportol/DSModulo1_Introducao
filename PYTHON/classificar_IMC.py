def calcularIMC(peso, altura):
    imc = peso/(altura * altura)
    if imc < 20:
        return 'abaixo do peso'
    elif imc <= 25:
        return 'peso normal'
    elif imc <= 30:
        return 'sobre peso'
    else:
        return 'obeso' 


peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
print(f'Resultado do IMC: {calcularIMC(peso,altura)}')