# 06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.



frase = input("Digite aqui uma frase: ")

for i in frase:
    if i.upper() == "A":
        continue
    elif i.upper() == "E":
        continue
    elif i.upper () == "I":
        continue
    elif i.upper() == "O":
        continue
    elif i.upper() == "U":
        continue
    
    print(i)


