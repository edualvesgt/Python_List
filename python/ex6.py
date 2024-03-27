# Solicita ao usuário o peso dos peixes
P = float(input("Informe o peso dos peixes em quilos: "))

# Verifica se há excesso
if P > 50:
    E = P - 50 # Calcula o excesso
    M = E * 4.0 # Calcula a multa
else:
    E = 0 # Não há excesso
    M = 0 # Não há multa

# Exibe os resultados
print("Excesso:", E, "quilos")
print("Multa: R$", M)
