# #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos

l = []
vezes = 1

while vezes <= 5:
    peso = float(input("Digite o seu peso aqui: "))
    vezes += 1
    l.append(peso)

print(f"O maior peso é {max(l)} KG.")
print(f"O menor peso é {min(l)} KG.")
