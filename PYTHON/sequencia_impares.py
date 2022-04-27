class SequenciaImpares:
    def exibirNumeros(x):
                  # range(star,stop,step)
        for num in range(1,x,2):
            print(num)


if __name__=='__main__':
    x = int(input("Digite o valor de x: "))
    SequenciaImpares.exibirNumeros(x)