class CalculoJogo:
    def calculaTempo(self, tempoInicial, tempoFinal):
        self.t_inicial = tempoInicial
        self.t_final = tempoFinal
        if self.t_final > self.t_inicial:
            resultado = tempoFinal - tempoInicial
            return resultado

if __name__=="__main__":
    tempo1 = int(input("Hora inicial: "))
    tempo2 = int(input("Hora final: "))
    jogo1 = CalculoJogo()
    print(f"O jogo durou {jogo1.calculaTempo(tempo1,tempo2)} hora(s)")
    
    