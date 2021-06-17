# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.


# a)
l = [5, 7, 2, 9, 4, 1, 3]

print(f"O tamanho da lista é {len(l)}")

# b) l

lista_maior_valor = max(l)
print(f"O maior valor da lista é {lista_maior_valor}")

# c)
lista_menor_valor = min(l)
print(f"O menor valor da lista é {lista_menor_valor}") 

# d
soma_da_lista = sum(l)
print(f"A soma de todos os valores da lista é {soma_da_lista}")

# e)
l.sort()
print(f"A ordem crescente dos números é {l}")

#f)
l.reverse()
print(f"A ordem decrescrente é {l}")
