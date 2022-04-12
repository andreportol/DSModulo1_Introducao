class Dardo:
    
    
    def exibirMaiorDistancia(a, b, c):
        if a > b and a > c:
            return a
        elif b > c:
            return b
        else:
            return c
        

if __name__=='__main__':
    print("Digite as três distancias:")
    a = float(input())
    b = float(input())
    c = float(input())
    print(f"Maior distancia: {Dardo.exibirMaiorDistancia(a, b, c)}")