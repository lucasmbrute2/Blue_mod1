from time import sleep
def retorna_again():
    return "Gostaria de jogar novamente ? "

def retorna_texto():
    return "\nVocê não concluiu o objetivo. \n~GAME OVER~"
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
        
        print('='*84)
        #Parte de validação da resposta

class Temporizador:
    def __init__(self):
        pass
    
    def atrasa_dialogo(self,dialogo):
        for i in dialogo:
            print(i,end="")
            sleep(0.006)
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

class Opcoes:
    def __init__(self,opcoes):
        self.opcoes = opcoes

    def retorna_dic(self):
        for c,v in self.opcoes.items():
            print(f"\n -Opção {c}: {v}")
            sleep(0.3)
    """É a função que retorna as opções de diálogo."""