# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela. 
# A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, 
# caso contrário é reprovado.
aluno = {}

nome = input("Digite aqui seu nome: ")
media = float(input("Digite aqui sua média: "))
aluno[nome] = media

if media >=7:
    situacao = "aprovado!!!"
elif media >=5 and media <7:
    situacao = "de recuperação."
else:
    situacao = "reprovado, estude mais."
aluno["situação"] = situacao

for c, v in aluno.items():
    if c ==nome:
        print(f"O aluno é {c} e sua média é {v}")
    else:
        print(f"Ele está {v}")

