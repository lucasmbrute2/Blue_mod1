# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def imc(altura,peso):
    imc =  peso / altura**2
    return f'Seu IMC é {imc:.2f}'


altura = float(input("Informe sua altura: "))
peso = float(input("Digite seu peso: "))

print(imc(altura,peso))