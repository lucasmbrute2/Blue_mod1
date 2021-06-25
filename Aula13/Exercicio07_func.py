# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais
def valor(n1,n2):
    if n1 >n2:
        print(f"{n1} é maior.")
    elif n1<n2:
        print(f"{n2} é maior")
    else:
        print("Os valores são iguais.")


valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite um segundo valor: "))
valor(valor1,valor2)