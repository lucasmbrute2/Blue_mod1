# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente , além da idade ,
#  com quantos anos a pessoa vai se aposentar.# Considere que o trabalhador deve contribuir 
# por 35 anos para se aposentar.
ano_atual = 2021
cadastro = {}
l= []
nome = input("Digite aqui o seu nome: ")   
ano_nascimento = int(input("Digite aqui o seu ano de nascimento: "))
l.append(ano_nascimento)
ctps = int(input("Digite aqui os anos trabalhados: "))
l.append(ctps)
idade = ano_atual - ano_nascimento 
l.append(idade)
if ctps !=0:
    l.append(int(input("Digite o ano em que você foi contratado: ")))
    l.append(float(input("Digite aqui o seu salário: ")))
    aposentar = (35 - ctps) + idade
    
cadastro[nome] = l
print(cadastro)
print(f"{nome} se aposentará com {aposentar} anos.")