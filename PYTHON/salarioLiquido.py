def imposto(valor):
    if valor <= 4000:
        return valor * 0.2
    else:
        return valor * 0.25


def previdencia(valor):
    if valor <= 1500:
        return valor * 0.1
    else:
        return valor * 0.15

def salarioLiquido(valor):
    salarioBruto = valor
    salarioLiquido =  salarioBruto - (previdencia(valor) + imposto(valor))
    return salarioLiquido


salarioBruto = float(input('Digite o valor do salário bruto: '))
print(f'Salário líquido: R$ {salarioLiquido(salarioBruto):.2f}')
