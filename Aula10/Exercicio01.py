# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela 
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' 
# e também quantos são maiores e quantos são menores de idade

lista_idade = list()
lista_nome = list()

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))   

for i in range(5):
    lista_idade.append(nome)
    lista_idade.append(idade)
    
    if idade >= 18:
        print(f"{nome} é maior de idade")
    else:  
        print(f"{nome} é menor de idade")


