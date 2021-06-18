# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

ano_atual = 2021
pessoas = 0
lista_anos = []
lista_under18 = 0
lista_above18 = 0

while pessoas < 2:
    lista_anos.insert(0,int(input("Digite o ano que você nasceu: ")))
    pessoas += 1

for i in lista_anos:
    i -= ano_atual 
    if i <= -18:
        lista_above18 +=1
        
    else:
        lista_under18 += 1
        
    
print(f"{lista_above18} pessoa(s) tem mais de 18 anos.")
print(f"{lista_under18} pessoa(s) tem menos de 18 anos.")
   

      
    

    


    
   