# # Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# # palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# # números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta


from random import randint

q_jogos = int(input("Quantos jogos você quer gerar? "))
cont = 0
l = []
l2_total= []

while cont < q_jogos:
    cont +=1
    l.clear()
    while len(l) <=6:
        num = randint(1,60)
        if num not in l:
            l.append(num)
        
    l2_total.append(l)

print(num)


print(l2_total)
    