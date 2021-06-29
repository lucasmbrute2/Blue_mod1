# Faça um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.
from time import sleep
from random import choice

l = ['televisao', 'jogar', 'amor', 'comida','cadeira','sentar', 'bola','cachorro','arroz', 'celular', 'maquiagem', 'joia']
erros_atual = 0
palavra_chave = choice(l)
tentativas = 6
letras_certas = []
letras_erradas = []

print('='*60)
print(f"Bem-Vindo ao jogo da forca!! Você só poderá errar {tentativas} vezes.")
print(f"A palavra oculta tem {len(palavra_chave)} letras.")

print("_"*len(palavra_chave))
juntar = " ".join(palavra_chave)
