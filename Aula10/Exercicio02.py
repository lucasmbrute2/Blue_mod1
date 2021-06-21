# 2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista, 
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o 
# programa. No final mostre:
# # Quantas pessoas foram cadastradas
# # Mostre a maior altura
# # Mostre a menor altura
total = 0
l = []
maior = 0
menor = 1000000000000
cont = 0
while True:
    total += 1
    nome = (input("Digite seu nome: "))
    l.append(nome)
    altura = (float(input("Digite sua altura: ")))
    l.append(altura)
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura 
    continuar = input("Você quer continuar ? ")
    if continuar.upper() == "SIM" or continuar.upper() == "S":
        continue
    else:
        break
print()   
print("Obrigado por participar!!")
print()
print(f"O total de pessoa(s) cadastrada(s) foi de: {total} pessoa(s).")
print(f"A menor altura foi: {menor} metros.")
print(f"A maior altura foi: {maior} metros.")