# # 1 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte 
# # quantas vezes aparece as vogais a,e,i,o,u


contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

frase = input('Digite uma frase: ')
for i in frase:
    if i.upper() == "A":   
        contador_a +=1
    if i.upper() == "E":
        contador_e += 1
    if i.upper() == "I":
        contador_i += 1
    if i.upper() == "O":
        contador_o += 1
    if i.upper() == "U":
        contador_u += 1

if contador_a >= 1:
    print(f"A vogal A aparece {contador_a} veze(s).")

if contador_e >= 1:
    print(f"A vogal aparece {contador_e} veze(s).")

if contador_i >= 1:
        print(f"A vogal I aparece {contador_i} veze(s).")

if contador_o >= 1:
    print(f"A vogal O aparece {contador_o} veze(s)")

if contador_u >= 1:
    print(f"A vogal aparece {contador_u} veze(s).")