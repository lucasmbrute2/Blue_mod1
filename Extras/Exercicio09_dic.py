# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A)Quantas pessoas cadastradas 
# B)A média de idaide. 
# C)Uma lista com mulheres. 
# D)Uma lista com idade acima da média.
lista_mulheres = []
lista_maior_idade = []
dic = {}
l = []
total = 0

while True:
    dic.clear()
    dic["nome"] = input("Digite aqui seu nome: ")
    while True:
        dic["sexo"] = input("Qual o seu sexo? ").upper()[0]
        if dic["sexo"] in ["F","M"]:
            break
        print("Não entendi o que você digitou, por favor repita")
    
    dic["idade"] = int(input("Digite a sua idade: "))
    l.append(dic.copy())  
    
    
    if dic['sexo'] == "F":
        lista_mulheres.append(dic["nome"])
    total += dic["idade"]
    media = total / len(l)
    if dic["idade"] > media:
        lista_maior_idade.append(dic["nome"])
    
    continuar = input("Você deseja continuar? ")
    if continuar in ["S","SIM","s","sim"]:
        continue
    else:
        break
    
print("="*30)
print(f"{len(l)} pessoa(s) cadastrada(s).")
print((f"A media das idades é {media:.0f}"))
print(f"As mulheres são {lista_mulheres}")
print(f"A(s) pessoa(s) acima da media da idade são/é: {lista_maior_idade}")
