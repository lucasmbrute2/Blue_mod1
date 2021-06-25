# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente , além da idade ,
#  com quantos anos a pessoa vai se aposentar.# Considere que o trabalhador deve contribuir 
# por 35 anos para se aposentar.
dic = {}
ano_atual = 2021

dic['Nome'] = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o ano em você nasceu: "))
dic['CTPS'] = int(input("Digite o número da sua carteira de trabalho (0 não tem): "))
dic['Idade'] = ano_atual - ano_nascimento
if dic['CTPS'] != 0:
    dic['Ano de contratação'] = int(input("Digite o ano em que você foi contratado: "))
    dic['Salário'] = float(input("Informe o seu salário: "))
    dic['Aposentadoria'] = 35 - (dic['Ano de contratação'] - ano_atual) + dic['Idade']
    
print("="*34)
for c, v in dic.items():
    print(f"{c}: {v}")

 