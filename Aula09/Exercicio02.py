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

# lista = []
# lista_par = []
# lista_impar = []                                                  #Aqui um caso onde nós perguntamos antes quantas vezes os usuário irá digitar o número.
# valor = int(input("Quantos valores você quer digitar ? "))
# for i in range(valor):
#     lista.append(int(input('Digite aqui o valor: ')))  
    
# for i in lista:
#     if i %2 ==0:
#         lista_par += [i]
#     else:
#         lista_impar +=[i]
    
# print(f"Aqui está a lista completa {lista}")
# print(f"Aqui estão os valores pares da lista {lista_par}")
# print(f"Aqui estão os valores ímpares da lista {lista_impar}")
