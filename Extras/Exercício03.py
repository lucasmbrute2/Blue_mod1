# Crie um programa onde o usuário possa digitar cinco valores numérios e cadestre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# # No final, mostre a lista ordenada na tela.

# l= []
# for i in range(5):
#     valor = int(input("Digite o valor: "))
#     l.insert(valor+1,valor)    
# print(l)

# Crie um programa onde o usuário possa digitar cinco valores numérios e cadestre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

l = []
for c in range(0, 5):
    aux = int(input('Digite o valor: '))
    if c == 0 or aux > l[-1]:
        l.append(aux)
        print(f'O valor {aux} foi adicionado na última posição')
    else:
        p = 0
        while p < len(l):
            if aux <= l[p]:
                l.insert(p, aux)
                print(f'O valor {aux} foi adicionado na posição {p}')
                break
            p += 1

print(f'Valores digitados: {l}')
