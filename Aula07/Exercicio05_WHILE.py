# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)

opcao = 0
while opcao <= 4:
    valor = int(input("Digite o primeiro valor aqui: "))
    valor2= int(input("Digite o segundo valor aqui: "))
    opcao = int(input("Escolha o que fazer:\n""[ 1 ] somar\n""[ 2 ] multiplicar\n""[ 3 ] maior\n""[ 4 ] novos números\n""[ 5 ] sair do programa\n"))
    if opcao == 1:
        print("Os valores são:",valor, "e" ,valor2,"")
        print("A soma dos valores é:",valor + valor2,"") 
    elif opcao == 2:
        print("Os valores são:",valor, "e" ,valor2,"")
        print(f"A multiplicação dos valores é: {valor * valor2}")
    elif opcao == 3:
        print("Os valores são:",valor, "e" ,valor2,"")
        if valor > valor2 :
            print("O primeiro valor é maior que o segundo. ")
        elif valor < valor2:
            print("O segundo valor é maior.")   
        else:
            print("Os valores são iguais.")
    elif opcao == 4:
        print("Ok. Digite os números novamente.")
        continue
print("Obrigado por participar!!")