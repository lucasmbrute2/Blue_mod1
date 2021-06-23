# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela. 
# A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, 
# caso contrário é reprovado.
l=[]
situacao_aluno = {}
situacao = ""
nome = input("Informe o seu nome: ")
nota = float(input("Informe a sua nota: "))
l.append(nota)
for i in l:    
    if nota >= 7:
        situacao = "aprovado!!" 
    elif nota <5:
        situacao = "reprovado :("
    else:
        situacao = "recuperação"    
l.append(situacao)
situacao_aluno[nome] = l
print(situacao_aluno)    
    


