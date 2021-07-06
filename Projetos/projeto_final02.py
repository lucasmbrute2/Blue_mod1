# A Vida de Joe 
# Contexto: 
# Joe é um viralata magricelo, que se perdeu de sua casa e vive numa viela no centro de belo horizonte. 
# Porém a gestão publica da cidade não permite animais de rua, e todos os dias a carrocinha passa procurando cachorros de rua para trancar nas gaiolas de um péssimo abrigo. Sua missão é levar joe de volta a sua casa, até as 18:00 horas, sem que ele seja pego pela malvada carrocinha de BH e sem passar por nenhuma dificuldade.
 
from time import sleep

def retorna_texto():
    return "Você não concluiu o objetivo. ~GAME OVER~"
    """Retorna 'game over para o usuário.'"""

        

      
class Temporizador:
    def __init__(self):
        pass
    
    def atrasa_dialogo(self,dialogo):
        for i in dialogo:
            print(i,end="")
            sleep(0.006)


class Horas:
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__(self):
        return f"São {self.horas:02d}:{self.minutos:02d}"
    
    
    def avanca_tempo(self,minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1


class Personagem:
    def __init__(self):

        self.sono = True
        self.fome = True
        self.sozinho = True
        self.sede = True
  
    def __str__(self):
        return f"-> {nome} {'está com sono' if self.sono else 'está descansado'}, {'está com fome' if self.fome else 'está alimentado'}, {'está sozinho' if self.sozinho else 'está acompanhado'} e {'está com sede' if self.sede else 'está saciado'}."

class Opcoes:
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
dic = {1: "Encontrar outro lugar para continuar dormindo.", 2: "Aguardar com sono a ONG abrir.",3: "Se esconder da carrocinha."}
opcoes = Opcoes(dic)
game_over = retorna_texto()

if __name__ == "__main__":
    while True:
        
        status = f"\n{personagem}"
        dialogo.atrasa_dialogo(f"{horas}. Você é um viralata magricelo, que se perdeu de casa e vive numa viela muito barulhenta, e para piorar (sempre pode piorar rs) a carrocinha passa as 6:30 recolhendo cachorros de rua. Seu nome é {nome} e você procura a sua casa todos os dias. Entretando a ONG em que você geralmente se alimenta abre as 7:00. O que deseja fazer agora?")
        print()
        dialogo.atrasa_dialogo(status)
        print()
        opcoes.retorna_dic()
        print('='*84)
        escolha = int(input("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n"))
        while dic.get(escolha,-1) == -1:
            # escolha = int(input("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n"))
            dialogo.atrasa_dialogo("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
            escolha = int(input())
            
        if escolha ==1:
            horas.avanca_tempo(720)
            dialogo.atrasa_dialogo(f"{horas} . {nome} descansou, mas passou muito mal por não ter se alimentado. Acabou seu tempo!\n")
            dialogo.atrasa_dialogo(game_over)
            break
        elif escolha ==2:
            dialogo.atrasa_dialogo("Ele aguarda abrir a ONG, porém fica muito visível e a carrocinha o encontra.")
            dialogo.atrasa_dialogo(game_over)
            break
        elif escolha ==3:
            horas.avanca_tempo(120)
            dialogo.atrasa_dialogo(f"{nome} ficou seguro, mas no caminho para casa, se deparou com uma bela fêmea, a cheirosa mais linda da cidade.")
            
            dic = {1:"Ir viver com o amor da sua vida nas ruas de BH, vivendo da sua arte.",2:" Não ir até a femêa e seguir a busca pela sua casa.",3:"Ir até a ONG e se alimentar. "}
            opcoes = Opcoes(dic)
            opcoes.retorna_dic()
            
            escolha = input("O que você quer fazer? ")
