# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta


from random import randint


jogos = int(input("Digite quantos jogos você deseja. "))
l= []
l_valores = []
for i in range(jogos):
    l = []
    while len(l) <=6:
        num = randint(1,60)
        if num not in l:
            l.append(num)
        
    l_valores.append(l)


    print(f" O jogo {i+1} saiu com os seguintes valores: {l_valores}")