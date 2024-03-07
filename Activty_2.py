#  2) Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão
# (em bits por segundo), informe o tempo necessário para o download do arquivo.
import time 

print("Vamos Calcular para fazer o upload do seu arquivo")
time.sleep(1)
# 1 MegaBit por segundo
VelocidadeBits = 1000000

TamanhoBits = float(input("Digite o tamanho do seu arquivo em BITS: "))

TempoUpload = TamanhoBits / VelocidadeBits

# Convertendo para minutos e segundos
TempoUploadMinutos = TempoUpload // 60
TempoUploadSegundos = TempoUpload % 60
time.sleep(3)
print(f"Tempo de Upload: {TempoUploadMinutos} minutos e {TempoUploadSegundos} segundos")
