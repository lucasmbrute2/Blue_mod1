# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
l = []
temp = []
for i in range(9):
    l.append(input('Digite aqui o valor: '))
    if len(l) ==3:
        temp.append(l[:])
        l.clear()
print("="*15)
for i in temp:
    print(i)
   
   
