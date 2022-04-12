from email.errors import InvalidDateDefect


class MediaIdades():
    def calcularMediaIdades():
        contador = 0
        soma_idade = 0
        
        print("Digite as idades:")
        idade = int(input())
        if idade < 0:
            print("IMPOSSIVEL CALCULAR")
        else:    
            while idade >= 0:
                contador += 1
                soma_idade += idade
                idade = int(input())
            print(f"MEDIA = {soma_idade/contador:.2f}")


if __name__=='__main__':
    MediaIdades.calcularMediaIdades()