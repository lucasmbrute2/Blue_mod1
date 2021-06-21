# #04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
# 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
# palpites diga ao jogador se o número do computador é maior ou menor ao que ele
# digitou,no final mostre quantos palpites foram necessários para vencer.


from random import randint
again = "Digite novamente:"
num = randint(0,10)
cont = 0
guess = int(input("Tente adivinhar o número entre 0 e 10 em que estou pensando: "))
cont = 0
while  guess <0 or guess >10:
        guess = int(input("Só vale números de 0 a 10, diga novamente."))

while True:
    cont +=1
    if guess>num:
        guess = int(input(f"Hmm, tente pensar em um valor menor. {again} "))
    elif guess<num:
        guess = int(input(f"Hmm, tente pensar um pouco mais alto. {again} "))
    else:
        print(f"Parabéns, você acertou!!Eu tinha pensado no número {num}")
        break
print(f"Você deu {cont} palpite(s) até acertar.")