
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(num1,num2,num3):
    soma = num1 + num2 + num3 
    return soma

num1 = int(input("Informe um número para ser somado: "))
num2 = int(input("Informe um número para ser somado: "))
num3 = int(input("Informe um número para ser somado: "))

print(soma(num1,num2,num3))