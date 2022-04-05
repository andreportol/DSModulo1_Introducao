class Coordenadas:
    
    def calculoCoordenadas(self,x,y):
        self.x = x
        self.y = y
        if x > 0 and y > 0:
            return "Primeiro quadrante"
        elif x > 0 and y < 0:
            return "Quarto quadrante"
        elif x < 0 and y > 0:
            return "Segundo quadrante"
        elif x < 0 and y < 0:
            return "Terceiro quadrante"
        elif x ==0 and y == 0:
            return "Origem"
        elif x == 0:
            return "Eixo y"
        elif y == 0:
            return "Eixo x"


coordenada = Coordenadas()
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
print(coordenada.calculoCoordenadas(x,y))