# Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
# - Produto indisponível
# - Produto Inválido
# - Quantidade solicitada não disponível.

estoque = {"vassoura": 3 ,"panela": 10, "arroz": 8, "salsisha": 15, "pão": 30, "chocolate": 6}

print("Bem-Vindo ao nosso supermercado, os nossos produtos são:\n-> [VASSOURA]\n-> [PANELA] \n-> [ARROZ] \n-> [SALSISHA] \n-> [PÃO] \n-> [CHOCOLATE]")

comprar = input("Digite o que você quer comprar: ").lower()
if comprar not in estoque:
    print("Produto inválido")

quantidade = int(input("Quantidade da compra: "))    

for i in estoque:
    if i == comprar:
        
        


print(estoque)