#  Faça um programa, com uma função que necessite de um argumento. 
#  A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def argumento(numero):
        if numero ==0:
            print("O valor é 0.")
        elif numero >1:
            print("O valor é positivo.")
        else: 
            print("O valor é negativo.")
       
n = int(input("Informe um valor: "))

argumento(n)
        