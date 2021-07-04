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
        self.quantidade_bomba = 50
     
        
    def alterar_combustivel(self,combustivel):
        
        self.tipo_combustivel = combustivel
        
    
    def alterar_valor(self,valor):
        self.valor_litro = valor
        restante = (self.quantidade_bomba - self.quantidade_combustivel/self.valor_litro)
        if restante <0:
            print(f"Infelizmente só temos disponível na bomba {self.quantidade_bomba} litros.")
        else:
            print(f"Foi abastecido R$ {self.quantidade_combustivel}. O tanque foi preenchido com {(self.quantidade_combustivel/self.valor_litro):.1f} litros.")
            
            print(f"A bomba ainda possui {restante:.1f} litros") 
        
    def alterar_quantidade_combustivel(self,quantidade):
        
        self.quantidade_combustivel = quantidade
        
        
    def abastecer_por_valor(self):
        restante = (self.quantidade_bomba - self.quantidade_combustivel/self.valor_litro)
        if restante <0:
            print(f"Infelizmente só temos disponível na bomba {self.quantidade_bomba} litros.")
        else:    
            print(f"Foi abastecido R$ {self.quantidade_combustivel} reais. O tanque foi preenchido com {(self.quantidade_combustivel/self.valor_litro):.1f} litros.")
            print(f"A bomba possui ainda {restante:.1f} litros.") 
        
        
    

   
    
    
      
gasolina = input("Com o que deseja abastecer ? [ETANOL] [GASOLINA]: ").lower()
valor = int(input("Com quantos reais deseja abastecer? "))
bomba = Bomba_combustivel("etanol", 4.50, valor )

if gasolina == "etanol":
    print("="*70)
    bomba.abastecer_por_valor()
    
else:
    print("="*70)
    bomba.alterar_combustivel("Gasolina")
    bomba.alterar_valor(5.10)
    bomba.alterar_quantidade_combustivel(valor)
    




    
    
    






