# Jogo de Ficção Interativa
# O que é ficção interativa?
# Ficção interativa, geralmente abreviada como IF, é um software de emulação de
# ambientes no qual os jogadores usam comandos de texto para controlar
# personagens do jogo e influenciar o ambiente.
# Escopo do projeto
# Em grupos de 2 ou 3 pessoas, crie um jogo de ficção interativa que simule a
# rotina diária de um personagem. Você pode escolher entre rotinas matinais,
# rotinas de trabalho, rotinas de estudos, entre outras. A ideia do jogo é que o
# jogador faça as escolhas para o seu personagem e o conduza durante o seu dia.
# Cada escolha irá gerar uma consequência diferente para o seu personagem. O
# jogo acaba quando o dia do seu personagem acabar. Você será responsável por
# determinar o inicio e término do dia do seu personagem, além de avançar o
# tempo a cada escolha.
# É obrigatório o uso de orientação a objetos (classes, encapsulamento e
# polimorfismo), funções, laços (while) e condicionais (if, elif, else). Para o
# desenvolvimento do jogo os grupos devem utilizar o arquivo disponibilizado no
# moodle como exemplo.
# Use toda sua criatividade para desenvolver uma história interessante e seja bem
# específico com relação as escolhas que precisam ser feitas, para que seu jogo
# seja divertido!

#De noite a bebida diminui os ml's mais rapido.
#A música influencia na quantidade de ml (ex: Sertenejo faz a bebida "trabalhar" mais).
#Quanto mais tempo passa melhor a bebida fica, tipo um vinho rs.
#Uma sociedade de bebidas, em que elas são premiadas por deixar o usuario embreagado.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A Vida de Joe 
 
# Contexto : Joe é um viralata magricelo, que se perdeu de sua casa e vive numa viela do centro de belo horizonte. Porém a gestão publica da cidade não permite animais de rua, e todos os dias a carrocinha passa procurando cachorros para trancar nas gaiolas de um péssimo abrigo. Sua missão é levar joe de volta a sua casa, sem que ele seja pego pela malvada carrocinha de BH. 
from time import sleep
class Opcoes:
    def __init__(self,opcoes):
        self.opcoes = opcoes
        
    def retorna_dic(self):
        for c,v  in self.opcoes.items():
            print(f"\n Opção -{c} : {v}")
            sleep(0.3)
    # def escolha(self,choose):
    #     if choose ==1:


class Temporizador:
    def __init__(self):
        pass
    
    def atrasa_dialogo(self,atrasa_dialogo):
        for i in atrasa_dialogo:
            print(i,end="")
            sleep(0.011)
       

        
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
        return f"--> {nome} está {'com sono' if self.sono  else 'sem sono'}, {'com fome' if self.fome else 'sem fome'}, {'com sede' if self.sede else 'hidratado'} e {'se sentindo sozinho.' if self.sozinho else 'se sentindo acolhido.'}"

dialogo = Temporizador()
nome = "Joe"
personagem = Personagem()
horas = Horas()

dic = {1: "Encontrar outro lugar para continuar dormindo.", 2: "Aguardar com sono a ONG abrir.",3: "Voltar a procurar sua casa. ",  4: "Se esconder da carrocinha."  }
opcoes = Opcoes(dic)
if __name__=="__main__":
    
    dia = 1
    descricao = f"{horas} do dia {dia}. Você é um viralata magricelo, que se perdeu de casa e vive numa viela muito barulhenta, e para piorar (sempre pode piorar rs) a carrocinha passa as 6:30 recolhendo cachorros de rua. Seu nome é {nome} e você procura a sua casa todos os dias. Entretando a ONG em que você geralmente se alimenta abre as 7:00. O que deseja fazer agora?"
    
    status = f"\n{personagem}"
    print('='*70)
    dialogo.atrasa_dialogo(descricao)
    print()
    dialogo.atrasa_dialogo(status)
    print()
    opcoes.retorna_dic()
    print('='*84)
    escolha = int(input("Digite a opção em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n"))
    opcoes.escolha(escolha)
    

