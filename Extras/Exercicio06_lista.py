# #Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A)Quantas pessoas foram cadastradas.
# B)Uma listagem com as pessoas mais pesadas. 
# C)Uma listagem com as pessoas mais leves

l = []
temp = []
maior = 0
menor = 0
while True:
    temp.append(input("Digite o seu nome aqui: "))
    temp.append(float(input("Digite o seu peso aqui: ")))
    if len(l) ==0:
        maior = menor = temp[1]
    if temp[1] > maior:
        maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    l.append(temp[:])
    temp.clear()
    continuar = input("Você quer continuar ? ")
    if continuar in ["S","SIM","s","sim"]:
        continue
    else:
        break
print("="*45)
print(f"O total de pessoas foi cadastradas foi {len(l)}")
for i in l:
    if i[1] == maior:
        print(f"A pessoas mais leve é {i[0]}, pesando {menor} KG")
    if i[1] == menor:
        print(f"A pessoas mais pesada é {i[0]}, pesando {maior} KG")    

    
    
