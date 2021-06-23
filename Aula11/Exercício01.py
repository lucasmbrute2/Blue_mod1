# 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) 
# e seus valores correspondentes aos quadrados desses números.

l = [1,4,5,6,7,9]
numeros_ao_quadrado = dict()
for i in l:
    numeros_ao_quadrado[i] = i**2
print(numeros_ao_quadrado)

print("="*69)
# b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] 
# e cada valor associado é o número ao quadrado.​

dicionario = {}
for i in range(1,11):
    dicionario[i] = i**2
print(dicionario)

