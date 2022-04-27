def multiplos(valor1,valor2):
    if valor1 == 0 or valor2 == 0:
        return "Digite valores diferente de zero"
    
    elif (valor1 > valor2) or (valor1 == valor2):
        if (valor1 % valor2) == 0:
           return "São multiplos."
        else:
            return "Nao sao multiplos."
    elif (valor1 < valor2):
        if valor2 % valor1 == 0:
           return "São multiplos."
        else:
            return "Nao sao multiplos." 

if __name__=="__main__":
    print("Digite dois numeros: ")
    valor1 = float(input())
    valor2 = float(input())
    print(multiplos(valor1,valor2))