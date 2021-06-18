# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a 
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)

cont = 0
n = float(input("Digite o número aqui : "))
cont += n
continuar = (input("Deseja continuar digitando os números ? [SIM / NÃO] "))
while continuar.upper().replace("s", "sim") == "SIM":
    n = float(input("Digite o número aqui : "))
    cont += n
    continuar = (input("Deseja continuar digitando os números ? [SIM / NÃO] "))
    if continuar.upper().replace("nao", "não" ) == "NÃO":
        print("Obrigado.")
        break         
print(f"A soma dos valores foi resultou em {cont}")
