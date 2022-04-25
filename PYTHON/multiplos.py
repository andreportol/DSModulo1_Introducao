class Multiplos:
    def __init__(self,num1, num2):
        if num1<num2:
            num1, num2 = num2, num1
        if num1 % num2 == 0:
            print('Sao Multiplos') 
        else:
            print('Nao sao Multiplos')
        
if __name__=='__main__':
    print('Digite dois numeros inteiros:')
    x = int(input())
    y = int(input())
    multi = Multiplos(x, y)
    