def calcular(valor):
    salario = valor
    if valor <= 1000:
        salarioNovo = salario + (valor * 0.2)
        return salarioNovo
    elif 1000 < valor and valor < 3000:
        salarioNovo = salario + (valor * 0.15)
        return salarioNovo
    elif 3000 < valor and valor < 8000:
        salarioNovo = salario + (valor * 0.10)
        return salarioNovo
    elif valor > 8000:
        salarioNovo = salario + (valor * 0.05)
        return salarioNovo


if __name__=="__main__":
    salario = float(input("Digite o salario da pessoa: "))
    print(f"Novo salario: {calcular(salario)}")
    print(f"Aumento: {calcular(salario) - salario}")
    print(f"Porcentagem: {((calcular(salario)/salario)- 1)*100:.2f}%")

