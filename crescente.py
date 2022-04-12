class Crescente:
    def verificarNumeros():
        a=0
        b=1
        while a != b:
            print("Digite dois numeros: ")
            a = int(input())
            b = int(input())
            if a > b:
                print("Decrescente!")
            elif b > a:
                print("Crescente!")
            

if __name__=='__main__':
    Crescente.verificarNumeros()
