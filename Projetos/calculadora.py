# Projeto da semana
# Caixa eletrônico

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#  As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#  O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

n1 = 1
n5= 5
n10 = 10
n50 = 50
n100 = 100
valor_restante = 0
valor_final = 0


valor_saque = int(input("Digite o valor do saque: "))
while valor_saque <10 or valor_saque >600:
    valor_saque = int(input("Valor indisponível. Digite um valor entre [10] e [600] "))


valor_restante = valor_saque//n100
valor_final = valor_saque - valor_restante*100

valor_restante = valor_saque//n50
valor_final = valor_saque - valor_restante*50
print(valor_final)

valor_restante = valor_saque//10
valor_final = valor_saque - valor_restante*10
print(valor_final)

valor_restante = valor_saque//5
valor_final = valor_saque - valor_restante*5
print(valor_final)

valor_restante = valor_saque//1
valor_final = valor_saque - valor_restante*1
print(valor_final)



