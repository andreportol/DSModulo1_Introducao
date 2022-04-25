class Operadora:

    def __init__(self, minutos):
        self.franquia = 100
        self.valorFranquia = 50
        self.valorMinuto = 2
        if minutos <= self.franquia:
            return print(f'Valor a pagar R$ {self.valorFranquia}')
        else:
            return print(f'Valor a pagar R$ {self.valorFranquia+(minutos - self.franquia)*self.valorMinuto}')

if __name__ == '__main__':
    minutos = int(input('Digite a quantidade de minutos: '))
    Vivo = Operadora(minutos)