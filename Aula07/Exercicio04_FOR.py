# #04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

l =[]
vezes = 0
lista_pares = []
while vezes <= 6:
    n = int(input("Digite aqui os números: "))
    vezes += 1
    l.append(n) 

print(l)
for i in l:
    if i%2 ==0:
        lista_pares += [i]

soma = sum(lista_pares)
print()
print(f"Foram digitados {len(lista_pares)} valores pares")
print(f"A soma dos valores pares é {soma}")