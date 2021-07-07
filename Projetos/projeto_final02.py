# A Vida de Joe 
# Contexto: 
# Joe é um viralata magricelo, que se perdeu de sua casa e vive numa viela no centro de belo horizonte. 
# Porém a gestão publica da cidade não permite animais de rua, e todos os dias a carrocinha passa procurando cachorros de rua para trancar nas gaiolas de um péssimo abrigo. Sua missão é levar joe de volta a sua casa, até as 18:00 horas, sem que ele seja pego pela malvada carrocinha de BH e sem passar por nenhuma dificuldade.
 
from time import sleep

def retorna_again():
    return "Gostaria de jogar novamente ? "

def retorna_texto():
    return "Você não concluiu o objetivo. \n~GAME OVER~"
    """Retorna 'game over para o usuário."""


class Respostas:
    def __init__(self):
        pass
        
    def resposta_errada(self,horas,dialogo,mensagem,gameover,again):
        dialogo.atrasa_dialogo(mensagem)
        
        dialogo.atrasa_dialogo(gameover)
        horas = Horas()
        
        print()
        print('='*40)
        dialogo.atrasa_dialogo(again)
        again = input().upper()[0]
        if again in ['S']:            
            return True
        else:
            dialogo.atrasa_dialogo("----OBRIGADO POR JOGAR----")
            return False
        
    def resposta_certa(self,horas,quant_horas,mensagem,dialogo,dic):

        horas.avanca_tempo(quant_horas)
        dialogo.atrasa_dialogo(mensagem)
        
        
        opcoes = Opcoes(dic)
        print()
        opcoes.retorna_dic()
        escolha = int(input("O que você quer fazer? "))
        print('='*84)
        #Parte de validação da resposta
        
        while dic.get(escolha,"batata") == "batata":
            dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
            escolha = int(input())
                #agora entra de fato na historia, a resposta correta
        return escolha





class Temporizador:
    def __init__(self):
        pass
    
    def atrasa_dialogo(self,dialogo):
        for i in dialogo:
            print(i,end="")
            # sleep(0.006)
    """ Função criada para deixar o diálogo aparecendo
    com uma letra de cada vez"""

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
    """ Manipulamos todo o tempo passado no jogo por essa função"""

class Personagem:
    def __init__(self):

        self.sono = True
        self.fome = True
        self.sozinho = True
        self.sede = True
  
    def __str__(self):
        return f"-> {nome} {'está com sono' if self.sono else 'está descansado'}, {'está com fome' if self.fome else 'está alimentado'}, {'está sozinho' if self.sozinho else 'está acompanhado'} e {'está com sede' if self.sede else 'está saciado'}."
    """É a função onde estão os atributos do nosso personagem, seu estado de saúde é manipulado por aqui."""

    def reset(self):
        self.sono = True
        self.fome = True
        self.sozinho = True



class Opcoes:
    def __init__(self,opcoes):
        self.opcoes = opcoes

    def retorna_dic(self):
        for c,v in self.opcoes.items():
            print(f"\n -Opção {c}: {v}")
            # sleep(0.3)
    """É a função que retorna as opções de diálogo."""

resposta = Respostas()
jogador = ""
personagem = Personagem()
dialogo = Temporizador()
nome = "Joe"
horas = Horas()
dic = {1: "Encontrar outro lugar para continuar dormindo.", 2: "Aguardar com sono a ONG abrir.",3: "Se esconder da carrocinha."}
opcoes = Opcoes(dic)
game_over = retorna_texto()
again = retorna_again()

if __name__ == "__main__":
    while True:
        jogador = input("Digite o nome do Player 1: ")
        status = f"\n{personagem}"
        dialogo.atrasa_dialogo(f"{horas}. Você é um viralata magricelo, que se perdeu de casa e vive numa viela muito barulhenta, e para piorar (sempre pode piorar rs) a carrocinha passa as 6:30 recolhendo cachorros de rua. Seu nome é {nome} e você procura a sua casa todos os dias. Entretando a ONG em que você geralmente se alimenta abre as 7:00. O que deseja fazer agora?")
        print()
        # dialogo.atrasa_dialogo(status)
        print()
        opcoes.retorna_dic()
        print('='*84)
        escolha = int(input("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n"))
        while dic.get(escolha,-1) == -1:
            dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
            escolha = int(input())

        if escolha ==1:
            mensagem = f"{nome} descansou, mas passou muito mal por não ter se alimentado. Acabou seu tempo!\n"
           
            if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                continue 
            else:
                break
            
        elif escolha ==2:
            
            mensagem = "Ele aguarda abrir a ONG, porém fica muito visível e a carrocinha o encontra.\n"
            
            if resposta.resposta_errada(horas,dialogo,mensagem,game_over):
                continue 
            else:
                break
            
        elif escolha ==3:
            
            dic = {1:"Ir viver com o amor da sua vida nas ruas de BH, vivendo da sua arte.",2:" Não ir até a femêa e seguir a busca pela sua casa.",3:"Ir até a ONG e se alimentar. "}
            mensagem = (f"{nome} ficou seguro, mas no caminho para casa, se deparou com uma bela fêmea, a cheirosa mais linda da cidade.")
            
            escolha = resposta.resposta_certa(horas,120,mensagem,dialogo)
            #Aqui atribuimos uma variavel para receber o return do objeto resposta. Isso
            #feito para a variavel escolha sempre estar atualizada.
            
            
            # horas.avanca_tempo(120)
            # dialogo.atrasa_dialogo(f"{nome} ficou seguro, mas no caminho para casa, se deparou com uma bela fêmea, a cheirosa mais linda da cidade.")
            # dic = {1:"Ir viver com o amor da sua vida nas ruas de BH, vivendo da sua arte.",2:" Não ir até a femêa e seguir a busca pela sua casa.",3:"Ir até a ONG e se alimentar. "}
            # opcoes = Opcoes(dic)
            # print()
            # opcoes.retorna_dic()
            # print('='*84)
            # escolha = int(input("O que você quer fazer? "))
            # #agora entra na parte de validação da resposta.
            # while dic.get(escolha,-1) == -1:
            #     dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
            #     escolha = int(input())
            # #agora entra de fato na historia, a resposta correta
            
            if escolha ==1:
                mensagem = f"Por {nome} ter ido até a femêa, ele curtiu muito seu relacionamento, que acabou durando 2 dias. O problema é que {nome} se afastou muito do local onde estava e ficou muito distante do seu caminho pra casa."
            
                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                    continue 
                else:
                    break
            

            elif escolha ==2:
                
                dic = {1:"Consumir a bebida alcoolica", 2:"Segurar a sede e caminhar até a fonte", 3:"Seguir seu caminho sem tomar água nenhuma."}
                mensagem = f"Agora já são {horas}, {nome} ainda não conseguiu encontrar o caminho de casa e está com muita sede, e pra piorar faz um sol de 39° Em BH. O problema, é que por estar na rua o unico liquido que joe encontrou foi o resto de uma bebida alcoolica que jogaram na rua, e a próxima fonte de agua publica está a 5km de distancia. E agora, o que joe deve fazer?"
                
                
                resposta.resposta_certa(horas,120,mensagem,dialogo)
                
                # horas.avanca_tempo(120)
                # dialogo.atrasa_dialogo(f"Agora já são {horas}, {nome} ainda não conseguiu encontrar o caminho de casa e está com muita sede, e pra piorar faz um sol de 39° Em BH. O problema, é que por estar na rua o unico liquido que joe encontrou foi o resto de uma bebida alcoolica que jogaram na rua, e a próxima fonte de agua publica está a 5km de distancia. E agora, o que joe deve fazer?")
                
                # dic = {1:"Consumir a bebida alcoolica", 2:"Segurar a sede e caminhar até a fonte", 3:"Seguir seu caminho sem tomar água nenhuma."}
                # opcoes = Opcoes(dic)
                # print()
                # opcoes.retorna_dic()
                # print('='*84)
                # #Parte de validação da resposta
                # escolha = int(input("O que você quer fazer? "))
                # while dic.get(escolha,"batata") == "batata":
                #     dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                #     escolha = int(input())
                #      #agora entra de fato na historia, a resposta correta
                #     if escolha ==1:
                #         horas.avanca_tempo(780)
                #         dialogo.atrasa_dialogo
            
            elif escolha ==3:
                mensagem = f"{nome} conseguiu se alimentar, mas por engano, a ONG serviu uma ração vencida. Infelizmente {nome} passou mal e ficou incapacitado o resto do dia e não achou seu lar a tempo."
                
                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                    continue 
                else:
                    break
           
            
        
        
        
                
            






                
                
               









print()           
dialogo.atrasa_dialogo(f"PARABÉNS {jogador}, VOCÊ VENCEU!! Joe chegou até sua casa, seus donos amaram! Deram a ele muita água boa, e comidas sensacionais. E sabe da melhor? O cachorro que ele viu de longe, era aquela femêa! A mais top de BH! Joe agradece muito seu esforço para ajuda-lo, até a próxima ;)  ")         
            
            
            
            
            
            