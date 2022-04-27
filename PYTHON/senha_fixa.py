class SenhaFixa:
    def validarSenha(self, valor):
        senha = "2002"
        if(senha == valor):
            print("Acesso permitido!")
            loop = False
            return loop
        else:
            loop = True
            return loop


if __name__=="__main__":
    senha = SenhaFixa()
    loop = True
    valor = input('Digite a senha: ')
    while(True):
        loop = senha.validarSenha(valor)
        if loop == False:
            break
        else:    
            valor = input("Senha inválida! Tente novamente: ")
