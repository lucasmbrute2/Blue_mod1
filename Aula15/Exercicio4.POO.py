# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

dic = {}
class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    
    def envelhecer(self):
        self.idade += 1
        dic["idade"] = self.idade
    def engordar(self):
        self.peso += 2                          #Tentei gaurdar o valor no dicionário e não consegui, cenas para os próximos capítulos.
        dic["Engordou"] = self.peso
    def emagrecer(self):
        self.peso -= 1
        dic["Emagreceu"] = self.peso
    
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
            dic["Altura"] = self.altura

while True:
    pessoas = Pessoa("Carlos", 15, 55.4, 1.67)
    pessoas.envelhecer()
    pessoas.engordar()
    pessoas.emagrecer()
    pessoas.crescer()
    print(vars(pessoas))
    
    continuar = input("A cada vez que você aperta 'enter' aumenta um ano, se quiser sair digite: [SAIR] ").upper()
    print(dic)
    print("="*90)
    if continuar == "SAIR":
        break
        
    