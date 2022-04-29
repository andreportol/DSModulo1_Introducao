num_casos = int(input('Quantos caso vc vai digitar?'))
if num_casos < 0:
    while(num_casos<0):
        print("Digite um numero positivo: ")
        num_casos = int(input())
else:
    for i in range(num_casos):
        print('Entre com o numerador: ')
        numerador = float(input())
        print('Entre com o denominador: ')
        denominador = float(input())
        if denominador == 0:
            print('DIVISAO IMPOSSIVEL')
        else:
            divisao = numerador / denominador
            print(f"Divisao = {divisao:.2f}")