# Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
def salario(n1,n2):
    salario = n1 *n2
    if n2 >= 40:
        extra = ((n2 - 40) * salario_hora) * 1.50
        salario += extra
    
    return salario

salario_hora = float(input("Digite o seu salário por hora aqui: "))
horas = int(input("Digite quantas horas você trabalhou na semana: "))

print(f"O seu salário semanal é: {salario(salario_hora,horas)}")

