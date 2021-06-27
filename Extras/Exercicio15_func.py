# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    cont = 1
    for i in range(num,0,-1):
        if show:
            print(i,end="")
            if i>1:
                print('x',end="")
            else:
                print('=',end='')
        cont *= i
    
    return cont
    
    
valor = int(input("Informe um valor para fazer o fatorial: "))
print(fatorial(valor,show=True))