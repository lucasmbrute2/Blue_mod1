# #02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

above18 = 0
man = 0
woman_under18 = 0


while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: [m] [f] ")
    if sexo.lower() == "m":
        man += 1
    if idade >= 18:
        above18 +=1
    if sexo.lower() == "f" and idade <20:
        woman_under18 +=1
    elif sexo.lower() == "f" and idade >0:
        pass
    elif sexo.lower() == "m" and idade >0:
        pass
    else: 
        print("Não entendi o que você digitou.")
    continuar = input("Você quer continuar ? [sim] [não] ")
    if continuar.upper() == "SIM":
        continue
    elif continuar.replace("nao", "não").replace("NAO", "NÃO").upper() == "NÃO":
      print("Obrigado por participar!")
      break
    else:
        print("Não entendi o que você digitou.")


print(f"{above18} pessoa(s) tem mais de 18 anos.")
print(f"Foram cadastrados {man} homen(s).")
print(f"{woman_under18} pessoas tem menos de 20 anos.")