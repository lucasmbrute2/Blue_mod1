# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o contéudo das três listas geradas.

l = []
l_pares = []
l_impares = []
while True:
    num = int(input("Digite o um valor: "))
    continuar = input("Você quer continuar? ")
    l.append(num)
    if continuar in ["S","sim","SIM","s"]:
        continue
    else:
        break
for i, v in enumerate(l):
    if v %2 == 0:
        l_pares.append(v)
    else:
        l_impares.append(v)
print('='*30)
print(f"A lista completa é: {l}")
print(f"A lista de pares é {l_pares}")
print(f"A lista de ímpares é {l_impares}")    


