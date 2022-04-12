class Dardo:
    
    
    def exibirMaiorDistancia(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        elif c > a and c > b:
            return c
        

if __name__=='__main__':
    print("Digite as três distancias:")
    a = float(input())
    b = float(input())
    c = float(input())
    print(f"Maior distancia: {Dardo.exibirMaiorDistancia(a, b, c)}")