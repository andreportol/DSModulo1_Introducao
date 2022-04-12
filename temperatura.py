import faulthandler


class Temperatura:
    def calcularTemperatura(escala):
        if escala == 'F':
            print("Digite a temperatura em Fahrenheit: ")
            valor = float(input())
            celsius = (5/9)*(valor - 32)
            print(f"Temperatura equivalente em Celsius: {celsius:.2f} ")
        elif escala == 'C':
            print("Digite a temperatura em Celsius: ")
            valor = float(input())
            fahre = ((9 * valor)/5)+32
            print(f"Temperatura equivalente em Fahrenheit: {fahre:.2f} ")
    

if __name__=='__main__':
    print("Voce vai digitar a temperatura em qual escala (C/F)?")
    escala = input()
    resultado = Temperatura.calcularTemperatura(escala)
    