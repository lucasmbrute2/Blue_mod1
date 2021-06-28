

# Crie um programa que tenha a função leialnt(), que vai funcionar de forma semelhante a funçã 
# input(), do Python, só que fazendo a validação para aceitar apenas um valor numérico.

# Ex:
# n = leiaInt("Digite um n")

def ficha(nome="<desconhecido>",gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato")

nome = input("Nome do Jogador: ")
gols = input("Número de Gols: ")
    
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() =="":
    ficha(gols=gols)
else:
    ficha(nome,gols)