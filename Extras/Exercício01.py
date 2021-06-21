#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas
#respectivas posições na lista.
l=[]
menor = 0
maior = 0
for i in range(5):
    l.append(int(input(f"Digite um número para ser listado na posição {i}: ")))
    if i == 0:
        menor = maior = l[i]
    elif l[i] > maior:
        maior = l[i]   
    elif l[i] <menor:
        menor = l[i]
print(f"A lista ficou assim: {l}")
for c , v in enumerate(l):
    if v == maior:
        print(f"O maior valor foi {v} na posição {c}")
for c, v in enumerate(l):
    if v == menor:
        print(f"O menor valor foi {v} na posição {c}")

