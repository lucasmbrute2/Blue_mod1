# A Vida de Joe 
# Contexto: 
# Joe é um viralata magricelo, que se perdeu de sua casa e vive numa viela no centro de belo horizonte. 
# Porém a gestão publica da cidade não permite animais de rua, e todos os dias a carrocinha passa procurando cachorros de rua para trancar nas gaiolas de um péssimo abrigo. Sua missão é levar joe de volta a sua casa, até as 18:00 horas, sem que ele seja pego pela malvada carrocinha de BH e sem passar por nenhuma dificuldade.
from time import sleep

import mod_projeto_final02 as mod

resposta = mod.Respostas()
jogador = ""
dialogo = mod.Temporizador()
nome = "Joe"
horas = mod.Horas()
dic = {1: "Encontrar outro lugar para continuar dormindo.", 2: "Aguardar com sono a ONG abrir.",3: "Se esconder da carrocinha."}
opcoes = mod.Opcoes(dic)
game_over = mod.retorna_texto()
again = mod.retorna_again()

if __name__ == "__main__":
    while True:
        horas = mod.Horas()
        jogador = input("Digite o nome do Player 1: ")
        # status = f"\n{personagem}"
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
        #bloco 1
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
            #bloco2
            dic = {1:"Ir viver com o amor da sua vida nas ruas de BH, vivendo da sua arte.",2:"Não ir até a femêa e seguir a busca pela sua casa.",3:"Ir até a ONG e se alimentar. "}
            mensagem = (f"{nome} ficou seguro, mas no caminho para casa, se deparou com uma bela fêmea, a cheirosa mais linda da cidade.")
            
            resposta.resposta_certa(horas,120,mensagem,dialogo,dic)
            #Aqui atribuimos uma variavel para receber o return do objeto resposta. Isso
            #feito para a variavel escolha sempre estar atualizada.
            escolha = int(input("O que você quer fazer? "))
            while dic.get(escolha,"batata") == "batata":
                dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                escolha = int(input())
                    #agora entra de fato na historia, a resposta correta
           
            
            if escolha ==1:
                mensagem = f"Por {nome} ter ido até a femêa, ele curtiu muito seu relacionamento, que acabou durando 2 dias. O problema é que {nome} se afastou muito do local onde estava e ficou muito distante do seu caminho pra casa."
            
                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                    continue 
                else:
                    break
            

            elif escolha ==2:
                
                dic = {1:"Consumir a bebida alcoolica.", 2:"Segurar a sede e caminhar até a fonte.", 3:"Seguir seu caminho com sede."}
                mensagem = f"Agora já são {horas}, {nome} ainda não conseguiu encontrar o caminho de casa e está com muita sede, e pra piorar faz um sol de 39° Em BH. O problema, é que por estar na rua o unico liquido que joe encontrou foi o resto de uma bebida alcoolica que jogaram na rua, e a próxima fonte de agua pública está a 5km de distancia."
                
                
                resposta.resposta_certa(horas,120,mensagem,dialogo,dic)
                escolha = int(input("O que você quer fazer? "))
                while dic.get(escolha,"batata") == "batata":
                    dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                    escolha = int(input())
                #bloco 3
                if escolha == 1:
                    mensagem =  f"{nome} tomou alguns goles de bebida e acabou gostando muito, decidiu viver no bar pensando na femêa e cantando modão."
                    
                    if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                        continue 
                    else:
                        break
                elif escolha ==2:
                    dic = {1:"Sentar a paulada no gato folgado.",2: "Compor uma música romântica, e tentar conquistar de uma vez por todas a femêa da sua vida.",3: "Meditar, assistir uma palestra de auto-ajuda e seguir o seu caminho sem confusão."}
                    mensagem = f"Deu tudo certo, {nome} se cansou um pouco mas conseguiu chegar até a fonte e saciar toda sua sede. O problema é que por ser uma fonte pública, outros animais também tomam aguá ali, e por consequência disso, {nome}se encontrou com um gato muito encrenqueiro!"  
                    
                    
                    resposta.resposta_certa(horas,120,mensagem,dialogo,dic)
                    escolha = int(input("O que você quer fazer? "))
                    while dic.get(escolha,"batata") == "batata":
                        dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                        escolha = int(input())
                    
                    if escolha ==1:
                        mensagem = f" {nome} bate no gato, e uma quadrilha de cachorros acha ele muito corajoso. {nome} foi convidado para entrar no PCC (Primeiro Comando dos Cachorrinhos) e entrando pro mundo do crime, não voltou mais pra casa!" 
                        
                        if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                            continue 
                        else:
                            break
                    elif escolha ==2:
                        mensagem = f"{nome} compôs a música, mas se esqueceu que não sabia cantar, passou muita vergonha e com o coração partido, não teve forças para seguir seu caminho." 
                        
                        if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                            continue 
                        else:
                            break
                
                    elif escolha ==3:
                        dic = {1:"Ele aguarda o sinal fechar, e atravessa rapidamente",2:"Ele vê os humanos atravessando sem que o sinal tenha fechado, e decide arriscar.",3:"Ele sai correndo desgovernadamente."}
                        
                        mensagem = f"{nome} tomou sua água e continuou a sua busca! Pela primeira vez reconheceu algo... Uma avenida principal, que sempre passeava com seus donos em suas caminhadas matinais. O problema é que por ser um local muito movimentado por automóveis, {nome} precisa dar algum jeito de atravessar." 
                        
                        resposta.resposta_certa(horas,120,mensagem,dialogo,dic)
                        escolha = int(input("O que você quer fazer? "))
                        while dic.get(escolha,"batata") == "batata":
                            dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                            escolha = int(input())
                        
                        if escolha ==1:
                            dic = {1:"Largar tudo de vez, ficar muito triste, e não voltar pra casa.", 2:"Arranjar outros donos, e postar no instagram que a favela venceu, esquece fio!!",3:"Ir até a sua casa mesmo assim, e entender o que realmente está acontecendo."}
                            
                            mensagem = f"{nome} coseguiu atravessar a avenida, e finalmente se deparou com a rua da sua casa, caminhando empolgado a encontrou! Ótimo né?!, talvez não... {nome}, de longe, notou outro cachorro dentro de sua casa brincando com seus donos..." 

                            resposta.resposta_certa(horas,120,mensagem,dialogo,dic)
                            escolha = int(input("O que você quer fazer? "))
                            while dic.get(escolha,"batata") == "batata":
                                dialogo.atrasa_dialogo("Digite uma opção válida em que você deseja seguir. Lembre-se que a sua escolha é irreversível.\n")
                                escolha = int(input())
                        
                            if escolha ==3:
                                mensagem = f"PARABÉNS {jogador}, VOCÊ VENCEU!! {nome} chegou até sua casa, seus donos amaram! Deram a ele muita água e comidas sensacionais. Sabe da melhor? O cachorro que ele viu de longe, era aquela femêa, a mais top de BH! {nome} agradece muito seu esforço para ajuda-lo, até a próxima ;)"
                                dialogo.atrasa_dialogo(mensagem)
                                
                                break
                                
                            elif escolha ==2:
                                mensagem = f"{nome} até tentou encontrar outros donos, o problema é que os unicos que ele encontrou eram os mesmos donos daquele gato muito encreiqueiro! Ele não ficou muito feliz..." 

                                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                                        continue 
                                else:
                                    break
                            
                            elif escolha ==1:
                                mensagem = f"{nome} ficou muito triste, terminou seu dia voltando pra viela e entrando para um grupoque acredita que a terra é plana."
                                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                                    continue 
                                else:
                                    break
                        
                        
                        elif escolha ==2:
                            mensagem = f"{nome} arriscou atravessar imprudentemente igual aos humanos, o problema é que ele quase causa um acidente! E o pior, o carro envolvido no acidente era o da carrocinha. Infelizmente joe foi levado para o abrigo! "
                
                            if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                                continue 
                            else:
                                break
                        elif escolha ==3:
                            mensagem = f"{nome} correu desgovernadamente, mas acabou quase sendo atingido por um dos automóveis, fique tranquilo(a)! ele não sentiu dor. O carro nem chegou perto, é que {nome} é muito medroso, acabou tendo um ataque e indo para o céu dos cachorrinhos."  
                            if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                                continue 
                            else:
                                break      
                
                
                elif escolha ==3:
                    mensagem = f" {nome} realmente precisava de água, até tentou seguir seu caminho, mas precisou desviar a rota a ver se encontrava outra fonte e infelizmente se perdeu." 
                    
                    if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                        continue 
                    else:
                        break
            
                    
            elif escolha ==3:
                mensagem = f"{nome} conseguiu se alimentar, mas por engano, a ONG serviu uma ração vencida, infelizmente  passou mal e ficou incapacitado o resto do dia e não achou seu lar a tempo."
                
                if resposta.resposta_errada(horas,dialogo,mensagem,game_over,again):
                    continue 
                else:
                    break

                
                
                        
            
            
            
            
            
            
            
            
            
            
           
            
        
        
        
                
            






                
                
               









         
            
            
            
            
            
            