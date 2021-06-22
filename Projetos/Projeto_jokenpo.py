# Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer; check//
# • Ler a minha escolha (Pedra, papel ou tesoura); check//
# • Decidir de forma aleatória a decisão do computador; check//
# • Mostrar quantas rodadas cada jogador ganhou;/check//
# • Determinar quem foi o grande campeão de acordo com a quantidade de check//
# vitórias de cada um (computador e jogador);/check//
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
# de quantidade de rodadas, se não finalize o programa.

from random import randint
l = ["Pedra" , "Papel", "Tesoura"]
programa = randint(0,2)
rounds = int(input('Digite quantas rodadas você quer jogar: '))
cont_player = 0
cont_bot = 0
for i in range(rounds):
    escolha = int(input("Digite qual a sua escolha: \n0 [PEDRA]\n1 [PAPEL]\n2 [TESOURA]\n"))
    print(f"O programa escolheu: {l[programa]}")
    if escolha == 0:
        print(f"Você escolheu: Pedra ")
    elif escolha ==1:
        print(f"Você escolheu: Papel ")
    elif escolha == 2:
        print(f"Você escolheu: Tesoura")
    if programa == 0:
        if escolha == 0:
            cont_player += 1
            cont_bot += 1
            print("Empate!")
        elif escolha ==1 :
            print("jogador venceu!!")
            cont_player += 1
        elif escolha ==2:
            print("A máquina venceu.")
            cont_bot += 1    
    if programa ==1:
        if escolha ==0:
            print("A máquina venceu.")
            cont_bot += 1
        elif escolha ==1:
            print("Empatou!")
            cont_bot += 1
            cont_player +=1
            
        elif escolha ==2:
            print("Você venceu!!!!")
            cont_player +=1        
    if programa ==2:
        if escolha ==0:
            print("Você venceu!!!!")
            cont_player +=1
                
        if escolha ==1:
            print("A máquina venceu.")
            cont_bot += 1    
        if escolha ==2:
            print("Empatou!")
            cont_bot += 1
            cont_player +=1       
    
if  cont_player > cont_bot:
    print("O grande vencedor foi o jogador.")
elif cont_player < cont_bot:
    print("O grande vencedor foi o programa.")
else:
    print("Empataram, joguem de novo :)")
        
