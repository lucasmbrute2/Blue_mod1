# 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) 
# e seus valores correspondentes aos quadrados desses números.
l = [1,4,5,6,7,9]
dicionario = dict()
    
for n in l:
    dicionario[n] = n**2

print(dicionario)

# b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

quadrados2 = {}

for i in range(1,11):
    quadrados2[i] = i**2

print(quadrados2)
