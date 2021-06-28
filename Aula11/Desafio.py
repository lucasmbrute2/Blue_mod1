# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário 
# se deseja continuar a resposta seja somente sim ou não.

def validacao(continuar):
    while True:
        if continuar not in  ["S","s","N","n"]:
            continuar = input("Por favor, digite [sim] ou [não]: ")
            continue
        else:
            break
   


dic = {}
l = []
woman_list = []
idades = 0
media = 0
acima_media = []
while True:
    dic.clear()
    dic["Nome"] = input("Digite o seu nome: ")
    dic["Sexo"] = input("Digite o seu sexo: ").upper()[0]
    if dic["Sexo"] in ["F","f"]:
        woman_list.append(dic["Nome"])
    dic["Idade"] = int(input("Digite a sua idade: "))
    idades += dic["Idade"]
    l.append(dic.copy())
    media = idades/len(l)
    
    if dic["Idade"] > media:
        acima_media.append(dic["Idade"])
   
    
    continuar = input("Você quer continuar cadastrando? ").upper()[0]
    validacao(continuar)
    if continuar in ["S","s"]:
        continue
    else:
        break   

    
    

print("="*50)
print(f"Estão cadastrada(s) {len(l)} pessoa(s).")
print(f"A média das idades é {media}")
print(f"A lista com as mulheres é : {woman_list}")
print(f"As idades acima da média são: {acima_media}")

