# # 02 - Desenvolva um código que pergunte um número n para o 
# # usuário e exiba todos seus divisores

n = int(input("Digite um número aqui: "))

for i in range(1,n +1):
  
    if n % i ==0:
    
        print(f" São divisores de {n} o(s) número(s) {i}")
    
