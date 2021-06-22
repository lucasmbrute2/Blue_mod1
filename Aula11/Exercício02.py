# Crie um programa, utilizade dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
# - Produto indisponível
# - Produto Inválido
# - Quantidade solicitada não disponível.

estoque = {"vassoura": 3 ,"panela": 10, "arroz": 8, "salsisha": 15}

while True:
    comprar = input("Digite o que você quer comprar: ")
    quantidade = int("Quantidade da compra: ")    
     