class Crescente:
    def verificarNumeros():
        print("Digite dois numeros: ")
        a= int(input())
        b= int(input())
        while a != b:
            if a > b:
                print("Decrescente!")
            else:
                print("Crescente!")
            print("Digite outros dois numeros: ")
            a = int(input())
            b = int(input())

if __name__=='__main__':
    Crescente.verificarNumeros()
