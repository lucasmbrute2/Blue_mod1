# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e 
# somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda 
# função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
# import importandoEx14
from random import randint
from time import sleep   


def sorteio(x):
    print('='*40)
    print(f"Sorteando 5 valores da lista")
    sleep(1)
    for i in range(5):
        n = randint(1,10)
        numeros.append(n)
    print(numeros,end="")
        
    
        
def somaPar(n):
    soma = 0
    for i in n:
        if i %2 ==0:
            soma += i
    print()
    print("="*40)
    print(f"A soma dos valores pares da lista é {soma}")

numeros = []
# importandoEx14 .
sorteio(numeros)
# importandoEx14.
somaPar(numeros)







 