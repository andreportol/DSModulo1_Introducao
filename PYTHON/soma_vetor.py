quantidade = int(input('Quantos números vc vai digitar: '))
lista_numeros = []
for posicao in range(quantidade):
    numero = float(input('Digite um número:'))
    lista_numeros.insert(posicao, numero)
soma = sum(lista_numeros)
media = sum(lista_numeros)/len(lista_numeros)
# Quando o 'end' não é usado, o Python por padrão completa com '\n' (quebra de linha)
print('VALORES = ', end = '')
for num in lista_numeros:
    print(num, end = '  ')
print('')
print(f'Soma= {soma:.2f}')
print(f'Media= {media:.2f}')