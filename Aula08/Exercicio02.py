# 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As 
# perguntas são:
#  "Telefonou para a vítima?"
#  "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  "Devia para a vítima?"
#  "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a 
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
# como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".




lista_perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?",
]

suspeita = 0


for i in lista_perguntas:
    resposta = input(f'Responda com "sim" ou "não. {i} ')
    if resposta == "sim":
      suspeita += 1

if suspeita < 2:
    print("Soltem esse palerma, ele é inocente..")
if suspeita == 2:
    print("Você é suspeito, estamos de olho.")
if suspeita >= 3 and suspeita <= 4:
    print("Você é cúmplice, está preso também!")
elif suspeita == 5:
    print("Ele é o assassino, prendam ele!!")

