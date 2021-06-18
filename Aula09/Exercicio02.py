# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.


lista = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    resposta = input("Deseja continuar: Digite [sim] ou [não]: ").lower()
    if resposta == "sim":
        continue
    else: 
        break
lista_par = []
lista_impar = []

for i in lista:
    if i%2 == 0:
        lista_par += [i]
    else:
        lista_impar += [i]
        
print(lista)
print(lista_par)
print(lista_impar)

