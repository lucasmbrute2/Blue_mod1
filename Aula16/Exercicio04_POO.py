# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# 
# 
# iii. alterarValor( ) – altera o valor do litro do combustível. //
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


    ##EXERCÍCIO TESTE##
class Bomba_Combustível():
    def __init__(self,quantidade_combustível):
        
        self.tipo_combustível = "Tipo de gasolina: Gasolina comum."
        self.valor_litro = "Valor da gasolina: 5.1 Reais"
        self.quantidade_combustível = "Você quer abastecer " + quantidade_combustível + " Reais."
        self.quantidade_bomba = 100

    def alterar_valor(self):
        self.quantidade_combustível = "Valor da gasolina: 4.5 Reais"
        return self.quantidade_combustível
    
    def alterar_combustivel(self):
        self.tipo_combustível = "Tipo de gasolina: Etanol."
        return self.tipo_combustível
    
    def alterar_quantidade(self,nova_quantidade):
        self.quantidade_combustível = "Você quer abastecer " + nova_quantidade + " Reais."
        return self.quantidade_combustível

#Exercícios feito com a manipulação de STRINGS, entretanto não informa quantos litros de gasolina irá entrar.


tipo_gasolina = input("Você quer abastecer com [Gasolina comum] ou [Etanol]\n ").lower()
valor = input("Quanto reais de combustível você gostaria de abastecer ?\n ")
bomba = Bomba_Combustível(valor)

if tipo_gasolina == "gasolina comum":
    for v in vars(bomba).values():
        print(f"{v}")
else:
    print('='*30)
    print(bomba.alterar_valor())
    print(bomba.alterar_combustivel())
    print(bomba.alterar_quantidade(valor))
    print('='*30)