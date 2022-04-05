def horaInicial(self, tempoInicial):
    self.tempoInicial = tempoInicial
    return self.tempoInicial

def horaFinal(self,tempoFinal):
    self.tempoFinal = tempoFinal
    return self.tempoFinal

def calculaTempo(self):
    if horaFinal() > horaInicial():
        return horaFinal() - horaInicial()

if __name__=="__main__":
    tempo1 = int(input("Hora inicial: "))
    tempo2 = int(input("Hora final: "))
    horaInicial(tempo1)
    horaFinal(tempo2)
    print(f" O jogo durou {calculaTempo} hora(s)")