#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno (largura e 
# comprimento) e mostre a área do terreno:
def area(largura,comprimento):
    area = largura*comprimento
    print(f"A área do terreno é de {area:.2f} metros")

largura = float(input("Digite aqui a largura: "))
comprimento = float(input("Digite aqui o comprimento: "))
area(largura,comprimento)