class tabuada:
    def exibirTabuada(valor):
        numero = valor
        # range (start, stop, step)
        for num in range(1,11,1):
            print(f'{numero} x {num} = {numero*num}')
    
    def solicitarNumero():
        pass


if __name__=='__main__':
    print("Deseja a tabuada para qual valor: ")
    numero = int(input())
    tabuada.exibirTabuada(numero)
