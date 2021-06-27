
from time import sleep


def autoriza_voto(ano_nascimento):
    """
    O voto, no Brasil, a partir dos 16 anos se torna opcional, e obrigatório aos 18 anos, qualquer idade inferior a essa caracteriza-se
    inelegibilidade para votar.
    """
    
    situacao = {0:"Voto negado.",1:"Voto opcional.",2:"Voto obrigatório."}
    if ano_nascimento >= 16 and ano_nascimento <18:
        ano_nascimento = 1
    elif ano_nascimento >=18:
        ano_nascimento = 2
    else:
        ano_nascimento = 0
    
    for i in situacao:
        if ano_nascimento == i:
            return situacao[i]


def votacao(acesso,voto):
    nulo = 0
    branco = 0
    he_man = 0
    thor = 0
    goku = 0
    maior = ""
    
    while True:
        if acesso == "Voto negado.":
            return print("Um(a) garotinh(a) como você não pode votar, vá para casa!")
        elif voto == 1:
            he_man += 1
        elif voto ==2:
            thor += 1
        elif voto ==3:
            goku +=1 
        elif voto ==4:
            nulo += 1
        else:
            branco +=1
        if he_man > thor and he_man > goku:
            maior = "He-man é o vencedor!!"
        elif thor > he_man and thor > goku:
            maior = "Thor é o vencedor!!"
        elif goku > thor and goku> he_man:
            maior = "Goku é o vencedor!!"
        else:
            maior = "Empate!!" 
        continuar = input("Mais algum cadastro? ").upper()[0]
        if continuar not in ['S','s']:
            return print("="*70),sleep(0.4),print("Votação encerrada."),sleep(0.4),print(f"He-mam recebeu {he_man} voto(s)."),sleep(0.5), print(f"Thor recebeu {thor} voto(s)."),sleep(0.5),print(f"Goku recebeu {goku} voto(s)."),sleep(0.5),print(f"Ao todo foram {nulo} voto(s) nulo(s)."),sleep(0.5),print(f"Ao todo foram {branco} voto(s) branco(s) "),sleep(0.5),print(f"O resultado da votação foi: {maior}")
        else:
            print('='*70)
            print("Os candidatos são: => 1 [He-Man]") 
            sleep(0.5)
            print("Os candidatos são: => 2 [Thor]")
            sleep(0.5)
            print("Os candidatos são: => 3 [Goku]")
            sleep(0.5)
            print("Os candidatos são: => 4 [NULO]")
            sleep(0.5)
            print("Os candidatos são: => 5 [Estou em cima do muro, logo, votarei em branco]")
            sleep(0.5)
            voto = int(input("Digite o número da opção: ")) 
            continue