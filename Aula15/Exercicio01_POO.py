# A) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade. 
# B)Acrescente a classe criada um método para mostrar os dados de uma pessoa. 
# C)Crie um objeto do tipo pessoa para testar suas propriedades e métodos

class Pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}")


pessoa = Pessoa("Lucas", "Souza", 21)

pessoa.mostrar_dados()
    