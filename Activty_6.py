#Calculo idade 

import time
from datetime import date


print("Vamos Calcular sua idade") 
print("")

time.sleep(1)

Idade = float(input("Qual seu ano de Nascimento:"))

AnoAtual = date.today().year

IdadePessoa = AnoAtual - Idade

IdadeFutura = 2030  - Idade  

time.sleep(3)
print(f" Sua idade hoje em dia é {IdadePessoa:.0f}, mas em 2030 você terá {IdadeFutura:.0f}")
