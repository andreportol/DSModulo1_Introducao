class Dentro_Fora:
    
    def calcular(self,valor_repeticao):
        self.contador_dentro = 0
        self.contador_fora = 0
        for num in range(valor_repeticao):
            numero = int(input('Digite um numero: '))
            if numero >=10 and numero <=20:
                self.contador_dentro += 1
            else:
                self.contador_fora += 1

    def exibir_resultado(self):
        print(f'{self.contador_dentro} Dentro')   
        print(f'{self.contador_fora} Fora') 

if __name__=="__main__":
    numero = int(input("Quantos numeros voce vai digitar: "))
    df = Dentro_Fora()
    df.calcular(numero)
    df.exibir_resultado()