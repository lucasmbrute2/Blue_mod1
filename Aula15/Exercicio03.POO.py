# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas 
# em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

from random import randint
from random import choice
l = ["cara", "coroa"]

class Numeros():
    def __init__(self,x):
        self.jogo = x
    
    
    def lançador(self):
        if self.jogo == "dado":
            dado = randint(1,6)
            print("="*42)
            print(f"O dado caiu com a face {dado} virada para cima.") 
            
        else:
            print("="*42)
            moeda = choice(l)
            print(f"O resultado da moeda deu: {moeda}")

dado_moeda = Numeros(input("Quer jogar o dado ou a moeda? "))

dado_moeda.lançador()

