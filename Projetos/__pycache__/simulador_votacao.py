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
import votacaofunc
from time import sleep
date = date.today()

aux = int(input("Digite o ano em que você nasceu: "))
data_nascimento = date.year - aux
permissao = votacaofunc.autoriza_voto(data_nascimento)
print(permissao)   
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

votacaofunc.votacao(permissao,voto)
    
    
            
            
        

          



         
    