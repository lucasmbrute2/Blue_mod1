# #Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A)Quantas pessoas foram cadastradas.
# B)Uma listagem com as pessoas mais pesadas. 
# C)Uma listagem com as pessoas mais leves

l = []
temp = []
maior = menor = 0
while True:
    temp.append(input("Digite o seu nome: "))
    temp.append(float(input("Digite o seu peso: ")))
    if len(l) == 0:
        maior = menor = temp[1]
    else:  
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    
    l.append(temp[:])
    continuar = input("Você quer continuar ? ")
    temp = []
    if continuar in ["N","Nao","n","não","NÃO","NAO","nao"]:
        break
    
print(f"Foram cadastradas {len(l)} pessoas.")
# print(f"As pessoas mais pesadas foram {[maior]}.")
for p in l:
    if p[1] == maior:
        print(f"{p[0]} é a pessoas mais pesada, pesando {maior}KG")
    elif p[1] == menor:
        print(f"{p[0]} é a pessoas mais leve, pesando {menor}KG.")

# print(f"As pessoas mais leves foram {[menor]}")
