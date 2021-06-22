# Crie um programa onde o usuário possa digitar vários valores numérios e cadestre-os em uma lista. Caso o número já exista lá dentro
# , ele NÃO será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente. 

# l = []
# continuar = "sim"
# while continuar.lower() == "sim" or continuar.lower() == "s":
#     num = (int(input("Digite aqui o número: ")))
#     if num not in l:
#         l.append(num)
#     continuar = input("Você deseja continuar ? ")
    
# l.sort()
# print(f"Todos os valores digitados em ordem crescente ficaram assim: {l}")

# # OUTRA FORMA MELHOR, PORÉM A LINHA 26 NÃO FUNCIONA:

l = []
while True:
    num = (int(input("Digite aqui o número: ")))
    if num not in l:
        l.append(num)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado, não vou adicionar.")
    continuar = (input("Você deseja continuar ? "))
    if continuar in ['N','n','Não','NÃO']:
        break

l.sort()
print(f"Todos os valores digitados em ordem crescente ficaram assim: {l}")