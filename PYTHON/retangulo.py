import cmath


def diagonal(base, altura):
    diagonal = cmath.sqrt((base * base) + (altura * altura))
    return diagonal

def area(base, altura):
    return base * altura

def perimetro(base, altura):
    return base * 2 + altura * 2


base = float(input('Digite o valor da base do retangulo: '))
altura = float(input('Digite o valor da altura do retangulo: '))
# ".real" serve para eliminar a parte imaginaria do número
print(f'Diagonal = {diagonal(base,altura).real:.2f}')
print(f'Area = {area(base,altura):.2f}')
print(f'Perimetro = {perimetro(base,altura):.2f}')
