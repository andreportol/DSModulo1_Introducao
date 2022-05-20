def realToDolar(quantia, cotacao):
    return quantia/cotacao


cotacao = float(input("Digite a cotação do dolar: "))
quantia = float(input("Digite a quantia em reais: "))
print(f'Você pode comprar {realToDolar(quantia,cotacao):.2f} dolares com esta quantia.')