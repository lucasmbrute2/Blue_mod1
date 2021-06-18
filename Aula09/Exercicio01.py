# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

l = []

while True:
    valor = int(input("Digite o valor aqui: "))
    if valor in l:
        print("Valor já informado, digite outro.")
    else: 
        l.append(valor) 
    resposta = input("Você quer continuar? [SIM / NÃO] ")

    if resposta == 'sim' or resposta == 's':
        continue
    else:
        break
  
l.sort()
print(l)

