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

class Bomba_combustivel:
    def __init__(self,tipo_combustivel,valor_litro,quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        
        self.litros = self.quantidade_combustivel/self.valor_litro
        self.quantidade_bomba = 50
    
    
    def abastecer_por_valor(self):
            print(f"Foi abastecido R$ {self.quantidade_combustivel}. O tanque foi preenchido com {self.litros:.1f} litros.")
            print(f"A bomba possui ainda {self.quantidade_bomba - self.litros:.2f} litros") 

    def abastecer_por_litro(self):
        
        print(f"O tanque será abastecido com {self.litros:.1f} litros. O valor será R$ {self.quantidade_combustivel}  ")
        
 
    


bomba = Bomba_combustivel("Etanol", 4.50, 50 )

bomba.abastecer_por_valor()

bomba.abastecer_por_litro()




