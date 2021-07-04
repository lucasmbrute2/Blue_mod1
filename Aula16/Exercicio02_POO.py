# Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.

class Ingresso:
    def __init__(self):
        self.preco = 15
        
    
    def imprimir_valor(self):
    
        return f"{self.preco} reais."
    
    

class IngressoVIP(Ingresso):
   
    def ingresso_vip(self):
        self.preco += 5
        
    
print("Olá, gostaria de comprar o ingresso comum ou VIP? ")

comum = Ingresso()
print(f"O preço do ingresso comum é {comum.imprimir_valor()}")
vip = IngressoVIP()
vip.ingresso_vip()
print(f"O preço do ingresso VIP é {vip.preco} reais.")