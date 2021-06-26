# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos 
# até que o usuário diga que não tem mais ninguém para votar, esse programa 
# precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como 
# parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que 
# virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, 
# caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela 
# pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.
from datetime import date
from time import sleep
date = date.today()
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

def votacao(permissao,voto):
    
    nulo = 0
    branco = 0
    he_man = 0
    thor = 0
    goku = 0
    mais_votado = ""
    while True:
        if permissao == "Voto negado":
            return "Um(a) garotinh(a) como você não pode votar, vá para casa!"
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
        continuar = input("Mais algum cadastro? ").upper()[0]
        if continuar not in ['S','s']:
            print("Votação encerrada.")
            return print("="*30), print(f"He-mam recebeu {he_man} voto(s)."), print(f"Thor recebeu {thor} voto(s)."),print(f"Goku recebeu {goku} voto(s)."), print(f"Ao todo foram {nulo} votos nulo(s)."),print(f"Ao todo foram {branco} votos branco(s) ")
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
        
           
         
        



aux = int(input("Digite o ano em que você nasceu: "))
data_nascimento = date.year - aux
print(autoriza_voto(data_nascimento))
while True: 
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
    if voto >= 1 and voto <= 5:
        break
    else:
        print("Por favor, digite um número entre 1 e 5")
        sleep(1)



votacao(data_nascimento,voto)
    