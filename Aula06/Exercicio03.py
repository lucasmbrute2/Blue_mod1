# 03 - Faça um script que o usuário escolha um número de início, 
# um número de fim, e um número de passo. O programa deve printar 
# todos os números do intervalo entre início e fim, "pulando" de 
# acordo com o intervalo passado.

numero_inicio = int(input("Digite o número de início: "))
numero_fim = int(input("Digite o número do fim: "))
numero_passo = int(input("Digte o número de passo: "))


for i in range(numero_inicio, numero_fim,numero_passo):
    print(i)
