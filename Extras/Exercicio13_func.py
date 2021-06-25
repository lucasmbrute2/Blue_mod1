# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(num):
    maior = 0
    if num > maior:
        maior = num
    return f"O maior valor é {maior}"
   

while True:
    valor = int(input("Digite o valor: "))
    maior(valor)
    continuar = input("Você quer continuar informando valores: ").upper()[0]
    if continuar in ['S']:
        continue
    else: 
        break
print(maior(valor))