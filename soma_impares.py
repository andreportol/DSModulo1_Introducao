class SomaImpares:
    def calcularSoma(self, num1, num2):
        if num1 > num2:
            numero1 = num1
            num1 = num2
            num2 = numero1
        num1 += 1
        soma = 0
        while num1 < num2:
            if (num1 % 2 != 0 and num1 < num2):
                soma += num1
            num1 += 1
        return soma
    
     
    def exiberValor(self,valor):
        print(f'Soma dos impares: {valor}')

if __name__=='__main__':
    c = SomaImpares()
    print("Digite dois numeros:")
    x = int(input())
    y = int(input())
    valor = c.calcularSoma(x,y)
    c.exiberValor(valor)

