# 4) Criar um algoritmo (Fluxograma) que leia o saldo de uma aplicação e imprimir
# o novo saldo, considerando um reajuste de 15%.
import time

print("Iremos Fazer o calculo dos imposto houve um reajuste ")
print("")

time.sleep(1)
while True: 
        try:  
            saldo = float (input('Digite o saldo: '))
            break
        except ValueError:
            print("Por favor, digite um valor numérico para o salário.")

# Calculo do Reajuste 
reajuste=saldo* (15/100)
reajusteatual=saldo+reajuste

time.sleep(3)
print(f"O novo saldo com o reajuste é de ${reajusteatual:.2f}")