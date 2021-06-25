# Faça um programa que tenha uma função chamada contador(), que receba três parâmentros: inicio, fim 
# e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:

# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2 
# C) Uma contagem personalizada

from time import sleep
def contador(x,y,z):
    print('='*31)
    print(f"Contagem de {x} até {y} de {z} em {z}:")
    # sleep(1.8)
    if z <0:
        z*= -1
    if z ==0:
        z =1
    if x <y:
        cont = x
        while cont <= y:
            print(f'{cont} ', end='')
            # sleep(0.15)
            cont += z
    else:
        cont = x
        while cont >= y:
            print(f"{cont} ", end='')
            # sleep(0.15)
            cont -= z
    
contador(1,10,1)
print()
contador(10,0,2)
print()
print("Agora é sua vez de personalizar a contagem! ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio,fim,passo)

print()
print("FIM!!")