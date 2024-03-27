# Solicita ao usuário os três valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Encontra o maior valor
if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

# Encontra o menor valor
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

# Calcula a média dos números
media = (a + b + c) / 3

# Arredonda a média para duas casas decimais
media = round(media, 2)

# Exibe os resultados
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média:", media)
