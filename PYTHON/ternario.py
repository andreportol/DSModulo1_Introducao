tempo = False
print('Hoje esta ' + ('calor.' if tempo else 'frio.'))
# outra modo
print('Hoje esta ' + ('frio.', 'calor.')[tempo])


preco = 34.5
desconto = ((preco * 0.1) if preco < 20 else preco * 0.05)
print(f'desconto: {desconto}')
            # False       # True
desconto = (preco * 0.05, preco * 0.1)[preco < 20]
print(f'desconto: {desconto}')