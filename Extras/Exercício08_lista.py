# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# l = []
# temp = []
# for i in range(9):
#     l.append(input('Digite aqui o valor: '))
#     if len(l) ==3:
#         temp.append(l[:])
#         l.clear()
# print("="*15)
# for i in temp:
#     print(i)
   
# OUTRA FORMA:

matriz = [[],[],[]]  
for l in range(0,3): 
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*15)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()

# Aprimore o desafio anterior, mostrando no final:
# A)A soma de todos os valores pares digitados.
# B)A soma dos valores da terceira coluna 
# C)O maior valor da segunda linha 

