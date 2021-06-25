# #03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.


total = 0
above1000 = 0                                                           
menor_valor = 1000000000000
nome_produto = ""
while True:
    produto = (input("Digite o nome do produto aqui: "))
    valor = float(input("Digite o valor do produto aqui: "))
    total += valor
    if valor < menor_valor:
        menor_valor = valor
        nome_produto = produto
    
    if valor > 1000:
        above1000 += 1
    
    continuar = input("Deseja continuar comprando ?\n ")
    if continuar.lower() == "sim":
        continue
    elif continuar.replace("nao","não").lower() == "não":
        print("Obrigado por utilizar nosso APP!")
        break
    else:
        while continuar.replace("nao","não").lower() != "não" and continuar.lower() != "sim":
            continuar = input("Não entendi a sua resposta, digite novamente. ")
        if continuar.replace("nao","não").lower() == "não":
            print("Obrigado por utilizar nosso APP!")
            break

print(f"O valor total gasto na compra foi de R$ {total:.2f} reais.")
print(f"{above1000} produtos custam mais de R$1000.00 reias.",)
print(f"O produto mais barato comprado foi: {nome_produto} por {menor_valor} reias.")