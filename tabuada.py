from numpy import integer


class tabuada:
    def exibirTabuada(valor):
        numero = valor
        for num in range(11):
            print(f'{numero} x {num} = {numero*num}')
    
    def solicitarNumero():
        pass


if __name__=='__main__':
    print("Deseja a tabuada para qual valor: ")
    numero = int(input())
    tabuada.exibirTabuada(numero)
