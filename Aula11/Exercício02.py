# Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
# - Produto indisponível
# - Produto Inválido
# - Quantidade solicitada não disponível.

estoque = {"vassoura": 3 ,"panela": 10, "arroz": 8, "salsisha": 15, "pão": 30, "chocolate": 6}
baixa_estoque = []
total_quantidade_geral = 0

continuar = input("Bem-vindo (a) ao Supermercado. Deseja ir as compras? (s/n) ").lower()
while continuar not in ['s', 'n']:
    continuar = input("Resposta inválida. Deseja ir as compras ? (s/n ").lower()

while continuar == 's':
    print("Bem-Vindo ao nosso supermercado, os nossos produtos são:\n-> [VASSOURA]\n-> [PANELA] \n-> [ARROZ] \n-> [SALSISHA] \n-> [PÃO] \n-> [CHOCOLATE]")
    comprar = input("O que você deseja comprar ? ")
    quantidade = int(input("Quantas unidades ? "))
    if comprar not in estoque:
        print("Produto inválido.")
    
    for i in estoque:
        
    continuar =  input("Deseja continuar comprando? [sim] [não] ").lower()[0]
    while continuar not in ['s', 'n']:
        continuar = input("Resposta inválida. Deseja ir as compras ? (s/n ").lower()





