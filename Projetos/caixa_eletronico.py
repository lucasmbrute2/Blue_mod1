# Projeto da semana
# Caixa eletrônico

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#  As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#  O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

n1 = 0
n5= 0
n10 = 0
n50 = 0
n100 = 0

valor_n1 = 1
valor_n2 = 5
valor_n3 = 10
valor_n4 = 50
valor_n5 = 100

valor_saque = int(input("Digite o valor do saque: "))
while valor_saque <10 or valor_saque >600:
    valor_saque = int(input("Valor indisponível. Digite um valor entre [10] e [600] "))

saque = valor_saque




n100 = saque//valor_n5
saque = saque - (n100*valor_n5)

n50 = saque//valor_n4
saque = saque - (n50*valor_n4)

n10 = saque//valor_n3
saque = saque - (n10*valor_n3)
n5 = saque//valor_n2
saque = saque - (n5*valor_n2)

n1 = saque//valor_n1
saque = saque - (n1*valor_n1)

print(f"O valor total do saque foi de R${valor_saque}\n")

if n100 >0:

    print(f"Foram sacadas {n100} nota(s) de {valor_n5} reais.")
if n50 >0:
    print(f"Foram sacadas {n50} nota(s) de {valor_n4} reais.")
if n10>0:
    print(f"Foram sacadas {n10} nota(s) de {valor_n3} reais.")
if n5>0:
    print(f"Foram sacadas {n5} nota(s) de {valor_n2} reais. ")
if n1 >0:
    print(f"Foram sacadas {n1} nota(s) de {valor_n1} real.")