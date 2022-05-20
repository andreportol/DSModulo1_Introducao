def calcularGlicose(valor):
    if valor <= 100:
        print('Classificação: Normal')
    elif valor <= 140:
        print('Classificação: Elevado')
    else:
        print('Classificação: Diabetes')


def calcularTrigliceridios(valor):
    if valor <=200:
        print('Classificação: Desejavel')
    else:
        print('Classificação: Aumentado')


def calcularColesterol(valor):
    if valor <=200:
        print('Classificação: Desejavel')
    elif valor <=240:
        print('Classificação: limiar')
    else:
        print('Classificação: Elevado')


glicose = float(input('Medida de glicose: '))
calcularGlicose(glicose)
trigliceridios = float(input('Medida de colesterol: '))
calcularTrigliceridios(trigliceridios)
colesterol = float(input('Medida de colesterol: '))
calcularColesterol(colesterol)