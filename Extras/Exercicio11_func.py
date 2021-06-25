# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmentro
# e mostre uma mensagem como tamanho adaptável.
# Ex: 
# escreva('Olá, Mundo!')

# saída:
# =========
# Olá,mundo!
# =========

def escreva(texto):
    print("="*len(texto))
    print(texto)
    print("="*len(texto))


escrever = input("Digite algum texto: ")

escreva(escrever)