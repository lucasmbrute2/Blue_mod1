# Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o
# volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro
# de faixas válidas.

class Televisao(): 
    def __init__(self,tv):
        self.tv = tv
    
        

    def volume_max_min(self,volume):
        
        while volume > 30 or volume <0:
            volume = int(input("Volume inválido, o volume máximo é 35 e o menor é 0. Selecione um valor disponível.  "))
        return f"O volume da televisão está em {volume}."
            
    
    def canal(self):
        while self.tv > 30 or self.tv <5:
            self.tv = int(input("Canal inválido, os canais disponíveis estão na faixa de 5 e 30. Escolha um desses: "))
        return f"A televisão está no canal {self.tv}."



tv = Televisao(int(input("Digite o canal que você deseja assistir: ")))
volume = int(input("Qual o volume em que você gostaria de deixar a televisão? "))

print(tv.canal())
print(tv.volume_max_min(volume))
