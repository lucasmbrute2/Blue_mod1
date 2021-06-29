# 2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

class Conta():

    def __init__(self,titular,saldo):

        self.titular = titular
        self.saldo = saldo

    
    def sacar(self,valor):
        self.saldo -= valor
    
    def depositar(self,valor):
        self.saldo += valor


conta = Conta("Lucas", 3500)

conta.sacar(1000)
print(f"O titular é {conta.titular} e seu saldo é: {conta.saldo}")