class Glicose:
    def calcularGlicose(self, valor_medido):
        if valor_medido <= 100:
            return print("Classificação: normal")
        elif valor_medido <= 140:
            return print("Classificação: elevado")
        else:
            return print("Classificação: diabetes")

if __name__=='__main__':
    valor = float(input("Digite a medida de glicose:"))
    g1 = Glicose()
    g1.calcularGlicose(valor)
    