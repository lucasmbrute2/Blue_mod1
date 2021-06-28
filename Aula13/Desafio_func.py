
# DESAFIO -  Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
#  Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
#  Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
#tryexcept
from datetime import date
def data(n):
    
    l = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5:"maio", 6: "junho", 7: "julho",8: "agosto",
    9: "setembro",10: "outubro",11: "novembro",12: "dezembro"}
    
    for i in l:
        if i == n:
            return l[i]

date = date.today()
data(date.month)
print(f"{date.day}/{data(date.month)}/{date.year}")