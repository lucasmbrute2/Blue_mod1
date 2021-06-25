#  Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
#   que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
#   A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    valor_final = taxaImposto + custo
    return valor_final


custo = float(input("Informe o custo do produto: "))
taxaImposto = int(input("Informe a porcentagem de imposto de incide sobre o produto: "))
custo_real = (taxaImposto/100) *custo
print("="*10)
print(f"O valor do produto com os impostos fica {somaImposto(custo,custo_real)} reais")