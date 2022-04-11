'''Podemos também calcular a raiz quadrada de um número complexo 
   em Python usando o método sqrt() do módulo cmath '''
from math import sqrt


class Baskara:
    
    def calcularValorDelta(self):
        self.delta = (b**2) - 4*(a * c)
        return self.delta
    
    def calcularValorX1(self, a, b, c):
        self.calcularValorDelta()
        x1 = (-b + sqrt(self.delta)) / (2 * a)
        return x1

    def calcularValorX2(self, a, b, c):
        x2 = (-b - sqrt(self.delta)) / (2 * a)
        return x2

    def validarCoeficienteA(self, a):
        while a <= 0:
            a = float(
                    input("Digite um valor para o coeficiente 'a' maior que zero: "))    
        return a

    def validarDelta(self):
        if self.calcularValorDelta() < 0:
            print("Delta negativo!! Não pode calcular.")
        else:
            print(f"Valor de X1: {bask.calcularValorX1(a, b, c)}")
            print(f"Valor de X2: {bask.calcularValorX2(a, b, c)}")


if __name__ == '__main__':
    bask = Baskara()
    a = float(input("Coeficiente a: "))
    bask.validarCoeficienteA(a)
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
    bask.validarDelta()
    
        
    
