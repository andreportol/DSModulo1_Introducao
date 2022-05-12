# criando vetores
vetorNomes = []
vetorTelefones = []
vetorTipos = []
vetorMinutos = []
# criando matriz tipo
matriz_tipo = []
for l in range(3):
    matriz_tipo.append(['']*2)

# preenchendo a matriz
matriz_tipo[0][0] = 25.5
matriz_tipo[0][1] = 0.10
matriz_tipo[1][0] = 35.0
matriz_tipo[1][1] = 0.12
matriz_tipo[2][0] = 60.0
matriz_tipo[2][1] = 0.15

# inserindo dados dos clientes nos vetores
def inserirDadosClientes(numero_clientes):
    for i in range(numero_clientes):
        print(f'Dados do {i+1}º cliente: ')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        tipo = int(input('Tipo: '))
        minuto = int(input('Minutos: '))
        vetorNomes.append(nome)
        vetorTelefones.append(telefone)
        vetorTipos.append(tipo)
        vetorMinutos.append(minuto)
    
# exibindo preço basico de cada tipo de conta
def exibirTipoConta():
    print('\nInforme o preço basico e excedente de cada tipo de conta: ')
    for l in range(3):
        print(f"Tipo {l}: ")
        for c in range(2):
            print(f'{matriz_tipo[l][c]:.2f}')

# Método para calcular conta
def calcularConta(tipo, minuto):  # franquia minutos = 90
    if(tipo == 0):
        if(minuto > 90):
            valorConta = (25.5 + ((minuto - 90)*0.1))
            return valorConta
        else:
            valorConta = 25.5
            return valorConta
    if(tipo == 1):
        if(minuto > 90):
            valorConta = (35.0 + ((minuto - 90)*0.12))
            return valorConta
        else:
            valorConta = 35.0
            return valorConta
    if(tipo == 2):
        if(minuto > 90):
            valorConta = (60.0 + ((minuto - 90)*0.15))
            return valorConta
        else:
            valorConta = 60.0
            return valorConta
    else:
        print('Tipo de conta digitado errado.')

# Relatório clientes
def exibirRelatorioClientes(numero_clientes):
    print('\nRELATÓRIO DE CLIENTES:\n')
    for i in range(numero_clientes):
        print(vetorNomes[i], end=', ')
        print(vetorTelefones[i], end=', ')
        print(f'Tipo {vetorTipos[i]}', end=', ')
        print(f'Minutos: {vetorMinutos[i]}', end=', ')
        print(f'Conta = R$ {calcularConta(vetorTipos[i], vetorMinutos[i]):.2f}')

if __name__=='__main__':
    numero_clientes = int(input("Informe a quantidade de clientes: "))
    inserirDadosClientes(numero_clientes)
    exibirTipoConta()
    exibirRelatorioClientes(numero_clientes)