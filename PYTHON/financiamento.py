def prestacao(total, entrada, meses):
    return (total - entrada)/meses

total = float(input('Valor total do imovel: '))
entrada = float(input('Valor pago na entrada: '))
meses = int(input('Será financiado em quantos meses? '))
print(f'Valor de cada prestação: {prestacao(total, entrada, meses):.2f}')