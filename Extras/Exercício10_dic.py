# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome 
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.No
# final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dic = {}
gols = []

dic['nome'] = input("Digite o nome do jogador: ")
dic['partidas'] = int(input(f"Quantas partidas {dic['nome']} jogou? "))

for v in range(1,(dic['partidas'])+1):
    gols.append(int(input(f"Quantos gols na partida {v}? ")))
dic['gols'] = gols[:]
print("="*54)
print(dic)
print("="*54)
for c,v in dic.items():
    print(f"{c}: {v}")
print("="*54)
