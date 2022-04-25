def menorValor(x,y,z):
    # criando lista vazia
    lista = []      
    lista.append(x)
    lista.append(y)
    lista.append(z)
    menor_numero = min(lista)
    return menor_numero

    
if __name__=='__main__':
    x = int(input("Primeiro valor: "))
    y = int(input("Segundo valor: "))
    z = int(input("Terceiro valor: "))
    print(f'Menor valor: {menorValor(x,y,z)}')