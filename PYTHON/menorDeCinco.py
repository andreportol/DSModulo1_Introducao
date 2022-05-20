def menorDeTres(x, y, z):
    if(x < y and x < z):
        return x
    if(y < z):
        return y
    else:
        return z

if __name__=='__main__':
    print("Digite cinco numeros: ")
    x = int(input())
    y = int(input())
    z = int(input())
    n1 = int(input())
    n2 = int(input())
    menor = menorDeTres(menorDeTres(x, y, z), n1,n2)
    print(f'menor número = {menor}')