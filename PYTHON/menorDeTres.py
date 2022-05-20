def menorDeTres(x, y, z):
    if(x < y and x < z):
        return x
    if(y < z):
        return y
    else:
        return z

if __name__=='__main__':
    print("Digite três numeros: ")
    x = int(input())
    y = int(input())
    z = int(input())
    menor = menorDeTres(x, y, z)
    print(f'menor número = {menor}')