# A Vida de Joe 
 
# Contexto : Joe é um viralata magricelo, que se perdeu de sua casa e vive numa viela do centro de belo horizonte. Porém a gestão publica da cidade não permite animais de rua, e todos os dias a carrocinha passa procurando cachorros para trancar nas gaiolas de um péssimo abrigo. Sua missão é levar joe de volta a sua casa, sem que ele seja pego pela malvada carrocinha de BH.
from time import sleep
class Temporizador():
    def __init__(self):
        pass
    
    def atrasa_dialogo(self,dialogo):
        for i in dialogo:
            print(i,end="")
            sleep(0.006)


class Horas():
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__(self):
        return f"São {self.horas:02d}:{self.minutos:02d}"


class Personagem():
    def __init__(self):

        self.sono = True
        self.fome = True
        self.sozinho = True
        self.sede = True
  
    def __str__(self):
        return f"-> {nome} {'está com sono' if self.sono else 'está descansado'}, {'está com fome' if self.fome else 'está alimentado'}, {'está sozinho' if self.sozinho else 'está acompanhado'} e {'está com sede' if self.sede else 'está saciado'}."

class Opcoes():
    def __init__(self,opcoes):
        self.opcoes = opcoes

    def retorna_dic(self):
        for c,v in self.opcoes.items():
            print(f"\n -Opção {c}: {v}")
            sleep(0.3)
personagem = Personagem()
dialogo = Temporizador()
nome = "Joe"
horas = Horas()
dic = {1: "Encontrar outro lugar para continuar dormindo.", 2: "Aguardar com sono a ONG abrir.",3: "Voltar a procurar sua casa. ",  4: "Se esconder da carrocinha."  }
opcoes = Opcoes(dic)

if __name__ == "__main__":
    dia = 1
    status = f"\n{personagem}"
    descricao = f"{horas} do dia {dia}. Você é um viralata magricelo, que se perdeu de casa e vive numa viela muito barulhenta, e para piorar (sempre pode piorar rs) a carrocinha passa as 6:30 recolhendo cachorros de rua. Seu nome é {nome} e você procura a sua casa todos os dias. Entretando a ONG em que você geralmente se alimenta abre as 7:00. O que deseja fazer agora?"
    dialogo.atrasa_dialogo(descricao)
    print()
    dialogo.atrasa_dialogo(status)
    print()
    opcoes.retorna_dic()
    print('='*84)
    escolha = int(input("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n"))