# <!-- lista = ["10",10,20,30,40,50,["Yago,["Glauco",True]]]

# for i, v enumarete(lista)

# "i" retornará os indices da lista, enquanto "v" os elementos. -->


# vingadores = {"Chris Evans":"Capitão América","Mark Ruffalo":"Hulk","Tom Hiddleston":"Loki", 
# "Chris Hemworth":"Thor","Robert Downey Jr":"Homem de Ferro","Scarlett Johansson":"Viúva Negra"}


# nome = input("Digite o nome da pessoa: ")
# print(vingadores.get(nome),"Não possui ninguem com esse nome.")

# print("Hulk" in vingadores.values()) #Teste se a string ''Hulk'' está nos valores.

#Para gerar novos valores a chave é só atribuir normalmente.

# vingadores["Robert Deniro"] = "Batman"

# print(vingadores)
# print(sorted(vingadores.keys()))

# ##Fazendo com input:
# # nome = input("Digite o nome do ator: ")
# # personagem = input("Digite o nome do personagem: ")
# # vingadores[nome] = personagem
# print(vingadores)

# #Removendo um valor:
# print()
# del vingadores["Mark Ruffalo"]
# print(vingadores)
# ator = input("Digite o nome do Ator: ")
# deletados = vingadores.pop(ator,"O ator não está na lista.")
# deletados = vingadores.pop(ator,"O ator não está na lista.")
# print()
# print(deletados)
# print(vingadores)
dic  = {}
menor = 0
maior = 0
for v in range(6):
    chave = input("Digite uma chave para o dicionário: ")
    valor = int(input("Digite um valor para o dic: "))
    if maior ==0:
        menor = maior = valor    
    if valor > maior:
        maior = valor
    elif valor <menor:
        menor = valor
    dic[chave] = valor
for c , v in dic.items():
    if v == maior:
        print(f"A pessoa mais velha é {c} com {v} anos")
    elif v == menor:
        print(f"A pessoa mais nova é {c} com {v} anos")
print(dic)
