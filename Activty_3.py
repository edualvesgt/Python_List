# 3) Criar um algoritmo (Fluxograma e Pseudocódigo) que calcule o consumo médio
# de um automóvel (medido em km/l), dado que são conhecidos a distância total
import time 

print("Iremos calcular o valor do Consumo do seu veiculo")
print("")
time.sleep(2)
DistanciaTotal = float(input("Informe a Distancia percorrida em km:"))
time.sleep(1)
VolumeDoCobustivel = float(input("Informe o volume de Combustivel consumido:"))
time.sleep(1)
# Calculo cpara ver Consumo medio 

ConsumoMedio = DistanciaTotal/VolumeDoCobustivel
time.sleep(3)
print(f"O Consumo medi do combustivel é de {ConsumoMedio:.2f} km/l")
