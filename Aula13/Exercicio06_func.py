# Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).


# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F

def nota(n):
    if n >=9.0:
        print("A")
    elif n >=8: 
        print("B")
    elif n >=7: 
        print("C")
    elif n >= 6: 
        print("D")
    else:
        print("F")
n = float(input("Digite aqui sua nota: "))
nota(n)