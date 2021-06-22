# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

l = []
cont = 0
while True:
    num = (int(input("Digite um valor: ")))
    l.append(num)
    cont += 1
    continuar = input("Você deseja continuar? ") 
    if continuar in ["N","n","Não","NÃO"]:
        break
l.sort(reverse=True)
print()
print(f"Foram digitados {cont} valores.")
print(f"Os valores em ordem decrescente são {l}.")
if 5 in l:
    print("O valor 5 foi digitado e está na lista. ")
else: 
    print(f"O valor 5 não faz parte da lista.")