tempo = False
print('Hoje esta ' + ('calor.' if tempo else 'frio.'))
# outra modo
print('Hoje esta ' + ('frio.', 'calor.')[tempo])