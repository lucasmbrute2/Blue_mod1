# Crie um programa onde o usuário possa digitar sete valoroes numéricos e cadestre-os em uma lista única
# que mantenha separados os valores pares e ímpares.No final, mostre os valores pares e ímpares em ordem 
# crescente.
# l = []
# l_pares = []
# l_impares = []
# for i in range(6):
#     l.clear()
#     n = int(input("Digite aqui os valores: "))
#     if n%2 ==0:
#         l_pares.append(n)
#     else:
#         l_impares.append(n)
#     l.append(l_pares[:])
#     l.append(l_impares[:])
# l_pares.sort()    
# l_impares.sort()
# print('='*40)
# print(f"Os valores pares são {l_pares}")
# print(f"Os valores ímpares são {l_impares}")    

# --------------------------------OU ENTÃO:
l = [[],[]]
valor = 0
for i in range(6):
    valor = int(input("Digite o valor aqui: "))
    if valor %2==0:
        l[0].append(valor)
    else:
        l[1].append(valor)
l[0].sort()
l[1].sort()
print(f"Os valores pares são {l[0]}")
print(f"Os valores ímpares são: {l[1]}")